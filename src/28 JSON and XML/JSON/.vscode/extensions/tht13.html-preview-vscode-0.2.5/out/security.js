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
const nls = require("vscode-nls");
const localize = nls.loadMessageBundle();
var HTMLPreviewSecurityLevel;
(function (HTMLPreviewSecurityLevel) {
    HTMLPreviewSecurityLevel[HTMLPreviewSecurityLevel["Strict"] = 0] = "Strict";
    HTMLPreviewSecurityLevel[HTMLPreviewSecurityLevel["AllowInsecureContent"] = 1] = "AllowInsecureContent";
    HTMLPreviewSecurityLevel[HTMLPreviewSecurityLevel["AllowScriptsAndAllContent"] = 2] = "AllowScriptsAndAllContent";
    HTMLPreviewSecurityLevel[HTMLPreviewSecurityLevel["AllowInsecureLocalContent"] = 3] = "AllowInsecureLocalContent";
})(HTMLPreviewSecurityLevel = exports.HTMLPreviewSecurityLevel || (exports.HTMLPreviewSecurityLevel = {}));
class ExtensionContentSecurityPolicyArbiter {
    constructor(globalState, workspaceState) {
        this.globalState = globalState;
        this.workspaceState = workspaceState;
        this.old_trusted_workspace_key = 'trusted_preview_workspace:';
        this.security_level_key = 'preview_security_level:';
        this.should_disable_security_warning_key = 'preview_should_show_security_warning:';
    }
    getSecurityLevelForResource(resource) {
        // Use new security level setting first
        const level = this.globalState.get(this.security_level_key + this.getRoot(resource), undefined);
        if (typeof level !== 'undefined') {
            return level;
        }
        // Fallback to old trusted workspace setting
        if (this.globalState.get(this.old_trusted_workspace_key + this.getRoot(resource), false)) {
            return HTMLPreviewSecurityLevel.AllowScriptsAndAllContent;
        }
        return HTMLPreviewSecurityLevel.Strict;
    }
    setSecurityLevelForResource(resource, level) {
        return this.globalState.update(this.security_level_key + this.getRoot(resource), level);
    }
    shouldAllowSvgsForResource(resource) {
        const securityLevel = this.getSecurityLevelForResource(resource);
        return securityLevel === HTMLPreviewSecurityLevel.AllowInsecureContent || securityLevel === HTMLPreviewSecurityLevel.AllowScriptsAndAllContent;
    }
    shouldDisableSecurityWarnings() {
        return this.workspaceState.get(this.should_disable_security_warning_key, false);
    }
    setShouldDisableSecurityWarning(disabled) {
        return this.workspaceState.update(this.should_disable_security_warning_key, disabled);
    }
    getRoot(resource) {
        if (vscode.workspace.workspaceFolders) {
            const folderForResource = vscode.workspace.getWorkspaceFolder(resource);
            if (folderForResource) {
                return folderForResource.uri;
            }
            if (vscode.workspace.workspaceFolders.length) {
                return vscode.workspace.workspaceFolders[0].uri;
            }
        }
        return resource;
    }
}
exports.ExtensionContentSecurityPolicyArbiter = ExtensionContentSecurityPolicyArbiter;
class PreviewSecuritySelector {
    constructor(cspArbiter, webviewManager) {
        this.cspArbiter = cspArbiter;
        this.webviewManager = webviewManager;
    }
    showSecuritySelectorForResource(resource) {
        return __awaiter(this, void 0, void 0, function* () {
            function markActiveWhen(when) {
                return when ? '• ' : '';
            }
            const currentSecurityLevel = this.cspArbiter.getSecurityLevelForResource(resource);
            const selection = yield vscode.window.showQuickPick([
                {
                    type: HTMLPreviewSecurityLevel.Strict,
                    label: markActiveWhen(currentSecurityLevel === HTMLPreviewSecurityLevel.Strict) + localize('strict.title', 'Strict'),
                    description: localize('strict.description', 'Only load secure content'),
                }, {
                    type: HTMLPreviewSecurityLevel.AllowInsecureLocalContent,
                    label: markActiveWhen(currentSecurityLevel === HTMLPreviewSecurityLevel.AllowInsecureLocalContent) + localize('insecureLocalContent.title', 'Allow insecure local content'),
                    description: localize('insecureLocalContent.description', 'Enable loading content over http served from localhost'),
                }, {
                    type: HTMLPreviewSecurityLevel.AllowInsecureContent,
                    label: markActiveWhen(currentSecurityLevel === HTMLPreviewSecurityLevel.AllowInsecureContent) + localize('insecureContent.title', 'Allow insecure content'),
                    description: localize('insecureContent.description', 'Enable loading content over http'),
                }, {
                    type: HTMLPreviewSecurityLevel.AllowScriptsAndAllContent,
                    label: markActiveWhen(currentSecurityLevel === HTMLPreviewSecurityLevel.AllowScriptsAndAllContent) + localize('disable.title', 'Disable'),
                    description: localize('disable.description', 'Allow all content and script execution. Not recommended'),
                }, {
                    type: 'moreinfo',
                    label: localize('moreInfo.title', 'More Information'),
                    description: ''
                }, {
                    type: 'toggle',
                    label: this.cspArbiter.shouldDisableSecurityWarnings()
                        ? localize('enableSecurityWarning.title', "Enable preview security warnings in this workspace")
                        : localize('disableSecurityWarning.title', "Disable preview security warning in this workspace"),
                    description: localize('toggleSecurityWarning.description', 'Does not affect the content security level')
                },
            ], {
                placeHolder: localize('preview.showPreviewSecuritySelector.title', 'Select security settings for HTML previews in this workspace'),
            });
            if (!selection) {
                return;
            }
            if (selection.type === 'moreinfo') {
                vscode.commands.executeCommand('vscode.open', vscode.Uri.parse('https://go.microsoft.com/fwlink/?linkid=854414'));
                return;
            }
            if (selection.type === 'toggle') {
                this.cspArbiter.setShouldDisableSecurityWarning(!this.cspArbiter.shouldDisableSecurityWarnings());
                return;
            }
            else {
                yield this.cspArbiter.setSecurityLevelForResource(resource, selection.type);
            }
            this.webviewManager.refresh();
        });
    }
}
exports.PreviewSecuritySelector = PreviewSecuritySelector;
