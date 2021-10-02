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
const vscode = require("vscode");
const path = require("path");
const file_1 = require("../util/file");
class OpenDocumentLinkCommand {
    constructor() {
        this.id = OpenDocumentLinkCommand.id;
    }
    static createCommandUri(path, fragment) {
        return vscode.Uri.parse(`command:${OpenDocumentLinkCommand.id}?${encodeURIComponent(JSON.stringify({ path, fragment }))}`);
    }
    execute(args) {
        const p = decodeURIComponent(args.path);
        return this.tryOpen(p, args).catch(() => {
            if (path.extname(p) === '') {
                return this.tryOpen(p + '.md', args);
            }
            const resource = vscode.Uri.file(p);
            return Promise.resolve(void 0)
                .then(() => vscode.commands.executeCommand('vscode.open', resource))
                .then(() => void 0);
        });
    }
    tryOpen(path, args) {
        return __awaiter(this, void 0, void 0, function* () {
            const resource = vscode.Uri.file(path);
            if (vscode.window.activeTextEditor && file_1.isHTMLFile(vscode.window.activeTextEditor.document) && vscode.window.activeTextEditor.document.uri.fsPath === resource.fsPath) {
                return this.tryRevealLine(vscode.window.activeTextEditor, args.fragment);
            }
            else {
                return vscode.workspace.openTextDocument(resource)
                    .then(vscode.window.showTextDocument)
                    .then(editor => this.tryRevealLine(editor, args.fragment));
            }
        });
    }
    tryRevealLine(editor, fragment) {
        return __awaiter(this, void 0, void 0, function* () {
            if (editor && fragment) {
                const lineNumberFragment = fragment.match(/^L(\d+)$/i);
                if (lineNumberFragment) {
                    const line = +lineNumberFragment[1] - 1;
                    if (!isNaN(line)) {
                        return editor.revealRange(new vscode.Range(line, 0, line, 0), vscode.TextEditorRevealType.AtTop);
                    }
                }
            }
        });
    }
}
OpenDocumentLinkCommand.id = '_html.openDocumentLink';
exports.OpenDocumentLinkCommand = OpenDocumentLinkCommand;
