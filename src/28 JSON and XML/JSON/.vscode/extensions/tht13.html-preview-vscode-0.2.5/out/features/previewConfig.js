"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
const vscode = require("vscode");
class HTMLPreviewConfiguration {
    static getForResource(resource) {
        return new HTMLPreviewConfiguration(resource);
    }
    constructor(resource) {
        const editorConfig = vscode.workspace.getConfiguration('editor', resource);
        const htmlConfig = vscode.workspace.getConfiguration('html', resource);
        const htmlEditorConfig = vscode.workspace.getConfiguration('[html]', resource);
        this.scrollPreviewWithEditor = !!htmlConfig.get('preview.scrollPreviewWithEditor', true);
        this.scrollEditorWithPreview = !!htmlConfig.get('preview.scrollEditorWithPreview', true);
        this.doubleClickToSwitchToEditor = !!htmlConfig.get('preview.doubleClickToSwitchToEditor', true);
        this.markEditorSelection = !!htmlConfig.get('preview.markEditorSelection', true);
        this.styles = htmlConfig.get('styles', []);
    }
    isEqualTo(otherConfig) {
        for (let key in this) {
            if (this.hasOwnProperty(key) && key !== 'styles') {
                if (this[key] !== otherConfig[key]) {
                    return false;
                }
            }
        }
        // Check styles
        if (this.styles.length !== otherConfig.styles.length) {
            return false;
        }
        for (let i = 0; i < this.styles.length; ++i) {
            if (this.styles[i] !== otherConfig.styles[i]) {
                return false;
            }
        }
        return true;
    }
}
exports.HTMLPreviewConfiguration = HTMLPreviewConfiguration;
class HTMLPreviewConfigurationManager {
    constructor() {
        this.previewConfigurationsForWorkspaces = new Map();
    }
    loadAndCacheConfiguration(resource) {
        const config = HTMLPreviewConfiguration.getForResource(resource);
        this.previewConfigurationsForWorkspaces.set(this.getKey(resource), config);
        return config;
    }
    hasConfigurationChanged(resource) {
        const key = this.getKey(resource);
        const currentConfig = this.previewConfigurationsForWorkspaces.get(key);
        const newConfig = HTMLPreviewConfiguration.getForResource(resource);
        return (!currentConfig || !currentConfig.isEqualTo(newConfig));
    }
    getKey(resource) {
        const folder = vscode.workspace.getWorkspaceFolder(resource);
        return folder ? folder.uri.toString() : '';
    }
}
exports.HTMLPreviewConfigurationManager = HTMLPreviewConfigurationManager;
