"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
// import { MarkdownIt, Token } from 'markdown-it';
const path = require("path");
const vscode = require("vscode");
const FrontMatterRegex = /^---\s*[^]*?(-{3}|\.{3})\s*/;
class MarkdownEngine {
    constructor() { }
    usePlugin(factory) {
        try {
            this.md = factory(this.md);
        }
        catch (e) {
            // noop
        }
    }
    getEngine(resource) {
        return __awaiter(this, void 0, void 0, function* () {
            if (!this.md) {
                // const hljs = await import('highlight.js');
                // const mdnh = await import('markdown-it-named-headers');
                // this.md = (await import('markdown-it'))({
                // 	html: true,
                // 	highlight: (str: string, lang: string) => {
                // 		// Workaround for highlight not supporting tsx: https://github.com/isagalaev/highlight.js/issues/1155
                // 		if (lang && ['tsx', 'typescriptreact'].indexOf(lang.toLocaleLowerCase()) >= 0) {
                // 			lang = 'jsx';
                // 		}
                // 		if (lang && hljs.getLanguage(lang)) {
                // 			try {
                // 				return `<div>${hljs.highlight(lang, str, true).value}</div>`;
                // 			} catch (error) { }
                // 		}
                // 		return `<code><div>${this.md!.utils.escapeHtml(str)}</div></code>`;
                // 	}
                // }).use(mdnh);
                for (const renderName of ['paragraph_open', 'heading_open', 'image', 'code_block', 'fence', 'blockquote_open', 'list_item_open']) {
                    this.addLineNumberRenderer(this.md, renderName);
                }
                this.addLinkNormalizer(this.md);
            }
            const config = vscode.workspace.getConfiguration('markdown', resource);
            this.md.set({
                breaks: config.get('preview.breaks', false),
                linkify: config.get('preview.linkify', true)
            });
            return this.md;
        });
    }
    stripFrontmatter(text) {
        let offset = 0;
        const frontMatterMatch = FrontMatterRegex.exec(text);
        if (frontMatterMatch) {
            const frontMatter = frontMatterMatch[0];
            offset = frontMatter.split(/\r\n|\n|\r/g).length - 1;
            text = text.substr(frontMatter.length);
        }
        return { text, offset };
    }
    render(document, stripFrontmatter, text) {
        return __awaiter(this, void 0, void 0, function* () {
            let offset = 0;
            if (stripFrontmatter) {
                const markdownContent = this.stripFrontmatter(text);
                offset = markdownContent.offset;
                text = markdownContent.text;
            }
            this.currentDocument = document;
            this.firstLine = offset;
            const engine = yield this.getEngine(document);
            return engine.render(text);
        });
    }
    addLineNumberRenderer(md, ruleName) {
        const original = md.renderer.rules[ruleName];
        md.renderer.rules[ruleName] = (tokens, idx, options, env, self) => {
            const token = tokens[idx];
            if (token.map && token.map.length) {
                token.attrSet('data-line', this.firstLine + token.map[0]);
                token.attrJoin('class', 'code-line');
            }
            if (original) {
                return original(tokens, idx, options, env, self);
            }
            else {
                return self.renderToken(tokens, idx, options, env, self);
            }
        };
    }
    addLinkNormalizer(md) {
        const normalizeLink = md.normalizeLink;
        md.normalizeLink = (link) => {
            try {
                let uri = vscode.Uri.parse(link);
                if (!uri.scheme && uri.path) {
                    // Assume it must be a file
                    const fragment = uri.fragment;
                    if (uri.path[0] === '/') {
                        const root = vscode.workspace.getWorkspaceFolder(this.currentDocument);
                        if (root) {
                            uri = vscode.Uri.file(path.join(root.uri.fsPath, uri.path));
                        }
                    }
                    else {
                        uri = vscode.Uri.file(path.join(path.dirname(this.currentDocument.path), uri.path));
                    }
                    if (fragment) {
                        uri = uri.with({
                            fragment
                        });
                    }
                    return normalizeLink(uri.with({ scheme: 'vscode-resource' }).toString(true));
                }
                else if (!uri.scheme && !uri.path && uri.fragment) {
                    return normalizeLink(uri.toString(true));
                }
            }
            catch (e) {
                // noop
            }
            return normalizeLink(link);
        };
    }
}
