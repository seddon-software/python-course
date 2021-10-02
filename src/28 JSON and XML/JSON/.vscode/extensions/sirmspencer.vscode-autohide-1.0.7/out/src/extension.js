"use strict";
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
const vscode_1 = require("vscode");
function activate(context) {
    if (vscode.workspace.getConfiguration("autoHide").hideOnOpen) {
        vscode.commands.executeCommand("workbench.action.closePanel");
        vscode.commands.executeCommand("workbench.action.closeSidebar");
    }
    ;
    vscode.window.onDidChangeTextEditorSelection(selection => {
        let config = vscode.workspace.getConfiguration("autoHide");
        let path = vscode.window.activeTextEditor.document.fileName;
        let pathIsFile = path.includes(".") || path.includes("\\") || path.includes("/");
        if (selection.kind != vscode_1.TextEditorSelectionChangeKind.Mouse // selection was not from a click
            || selection.selections.length != 1 // no selections or multiselections
            || selection.selections.find(a => a.isEmpty) == null // multiselections
            || !pathIsFile) { // The debug window editor
            return;
        }
        else {
            setTimeout(function () {
                if (config.autoHidePanel) {
                    vscode.commands.executeCommand("workbench.action.closePanel");
                }
            }, config.panelDelay);
            setTimeout(function () {
                if (config.autoHideSideBar) {
                    vscode.commands.executeCommand("workbench.action.closeSidebar");
                }
            }, config.sideBarDelay);
        }
        ;
    });
    context.subscriptions.push(vscode.commands.registerCommand("autoHide.toggleHidePanel", () => __awaiter(this, void 0, void 0, function* () {
        let config = vscode.workspace.getConfiguration("autoHide");
        yield config.update("autoHidePanel", !config.autoHidePanel, vscode.ConfigurationTarget.Workspace);
    })));
    context.subscriptions.push(vscode.commands.registerCommand("autoHide.toggleHideSideBar", () => __awaiter(this, void 0, void 0, function* () {
        let config = vscode.workspace.getConfiguration("autoHide");
        yield config.update("autoHideSideBar", !config.autoHideSideBar, vscode.ConfigurationTarget.Workspace);
    })));
}
exports.activate = activate;
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map