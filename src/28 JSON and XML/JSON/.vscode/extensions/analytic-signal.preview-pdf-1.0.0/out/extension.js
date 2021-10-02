"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
const PDFEditorProvider_1 = require("./PDFEditorProvider");
function activate(context) {
    //
    // register custom editor provider:
    //
    context.subscriptions.push(PDFEditorProvider_1.PDFEditorProvider.register(context));
}
exports.activate = activate;
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map