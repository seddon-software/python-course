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
function showPreview(webviewManager, uri, previewSettings) {
    return __awaiter(this, void 0, void 0, function* () {
        let resource = uri;
        if (!(resource instanceof vscode.Uri)) {
            if (vscode.window.activeTextEditor) {
                // we are relaxed and don't check for html files
                resource = vscode.window.activeTextEditor.document.uri;
            }
        }
        if (!(resource instanceof vscode.Uri)) {
            if (!vscode.window.activeTextEditor) {
                // this is most likely toggling the preview
                return vscode.commands.executeCommand('html.showSource');
            }
            // nothing found that could be shown or toggled
            return;
        }
        const resourceColumn = (vscode.window.activeTextEditor && vscode.window.activeTextEditor.viewColumn) || vscode.ViewColumn.One;
        webviewManager.preview(resource, {
            resourceColumn: resourceColumn,
            previewColumn: previewSettings.sideBySide ? resourceColumn + 1 : resourceColumn,
            locked: !!previewSettings.locked
        });
    });
}
class ShowPreviewCommand {
    constructor(webviewManager) {
        this.webviewManager = webviewManager;
        this.id = 'html.showPreview';
    }
    execute(mainUri, allUris, previewSettings) {
        for (const uri of Array.isArray(allUris) ? allUris : [mainUri]) {
            showPreview(this.webviewManager, uri, {
                sideBySide: false,
                locked: previewSettings && previewSettings.locked
            });
        }
    }
}
exports.ShowPreviewCommand = ShowPreviewCommand;
class ShowPreviewToSideCommand {
    constructor(webviewManager) {
        this.webviewManager = webviewManager;
        this.id = 'html.showPreviewToSide';
    }
    execute(uri, previewSettings) {
        showPreview(this.webviewManager, uri, {
            sideBySide: true,
            locked: previewSettings && previewSettings.locked
        });
    }
}
exports.ShowPreviewToSideCommand = ShowPreviewToSideCommand;
class ShowLockedPreviewToSideCommand {
    constructor(webviewManager) {
        this.webviewManager = webviewManager;
        this.id = 'html.showLockedPreviewToSide';
    }
    execute(uri) {
        showPreview(this.webviewManager, uri, {
            sideBySide: true,
            locked: true
        });
    }
}
exports.ShowLockedPreviewToSideCommand = ShowLockedPreviewToSideCommand;
