import random
from datetime import datetime
import os
import re
import json

# Comprehensive list of VS Code extensions with exactly 10 per category
extensions_by_category = {
    "Code Quality & Formatting": [
        {
            "name": "Prettier - Code formatter",
            "id": "esbenp.prettier-vscode",
            "overview": "Prettier is an opinionated code formatter that enforces a consistent style by parsing your code and re-printing it with its own rules, supporting many languages and integrating with most editors.",
            "tags": ["formatter", "code-quality", "javascript", "typescript", "css", "html"]
        },
        {
            "name": "ESLint",
            "id": "dbaeumer.vscode-eslint",
            "overview": "ESLint is a popular linter for JavaScript and TypeScript that helps you find and fix problems in your code, enforcing coding standards and best practices.",
            "tags": ["linter", "javascript", "typescript", "code-quality"]
        },
        {
            "name": "SonarLint",
            "id": "SonarSource.sonarlint-vscode",
            "overview": "SonarLint helps you detect and fix quality issues as you write code. Like a spell checker, SonarLint squiggles quality issues and provides real-time feedback.",
            "tags": ["code-quality", "security", "bugs", "code-smells"]
        },
        {
            "name": "Code Spell Checker",
            "id": "streetsidesoftware.code-spell-checker",
            "overview": "Code Spell Checker is a basic spell checker that works well with code and documents, helping you catch common spelling errors in comments and strings.",
            "tags": ["spell-check", "documentation", "comments"]
        },
        {
            "name": "Stylelint",
            "id": "stylelint.vscode-stylelint",
            "overview": "Stylelint is a mighty, modern CSS linter that helps you enforce consistent conventions and avoid errors in your stylesheets.",
            "tags": ["css", "linter", "style", "code-quality"]
        },
        {
            "name": "Black Formatter",
            "id": "ms-python.black-formatter",
            "overview": "Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting.",
            "tags": ["python", "formatter", "code-quality", "black"]
        },
        {
            "name": "RuboCop",
            "id": "rebornix.Ruby",
            "overview": "RuboCop is a Ruby static code analyzer and formatter, out of the box it will enforce many of the guidelines outlined in the community Ruby Style Guide.",
            "tags": ["ruby", "linter", "formatter", "code-quality"]
        },
        {
            "name": "PHP CS Fixer",
            "id": "junstyle.php-cs-fixer",
            "overview": "PHP CS Fixer is a tool to automatically fix PHP coding standards issues. It can fix most issues in your code to follow PSR-1 and PSR-2 coding standards.",
            "tags": ["php", "formatter", "code-quality", "psr"]
        },
        {
            "name": "Rust Analyzer",
            "id": "rust-lang.rust-analyzer",
            "overview": "Rust Analyzer is an implementation of Language Server Protocol for Rust, providing features like go to definition, find all references, and more.",
            "tags": ["rust", "language-server", "intellisense", "code-quality"]
        },
        {
            "name": "EditorConfig",
            "id": "EditorConfig.EditorConfig",
            "overview": "EditorConfig helps developers define and maintain consistent coding styles between different editors and IDEs.",
            "tags": ["editor-config", "coding-style", "consistency", "code-quality"]
        }
    ],
    
    "Git & Version Control": [
        {
            "name": "GitLens — Git supercharged",
            "id": "eamodio.gitlens",
            "overview": "GitLens supercharges the built-in VS Code Git capabilities, providing rich insights into code authorship, history, and more, right in your editor.",
            "tags": ["git", "version-control", "history", "blame"]
        },
        {
            "name": "Git Graph",
            "id": "mhutchie.git-graph",
            "overview": "Git Graph is a powerful extension that visualizes your Git repository with a beautiful graph, making it easy to understand your project's history.",
            "tags": ["git", "visualization", "history", "graph"]
        },
        {
            "name": "Git History",
            "id": "donjayamanne.githistory",
            "overview": "Git History allows you to view the git log, file history, compare branches or commits, and more, all within VS Code.",
            "tags": ["git", "history", "log", "compare"]
        },
        {
            "name": "Git Blame",
            "id": "waderyan.gitblame",
            "overview": "Git Blame shows git blame information in the status bar for the currently selected line.",
            "tags": ["git", "blame", "history", "authorship"]
        },
        {
            "name": "GitHub Pull Requests and Issues",
            "id": "GitHub.vscode-pull-request-github",
            "overview": "Review and manage GitHub pull requests and issues directly in VS Code.",
            "tags": ["github", "pull-requests", "issues", "git"]
        },
        {
            "name": "GitDoc",
            "id": "vscode-gitdoc.gitdoc",
            "overview": "GitDoc automatically commits and pushes your changes to a git repository, so you never lose your work.",
            "tags": ["git", "auto-commit", "backup", "version-control"]
        },
        {
            "name": "GitHub Repositories",
            "id": "GitHub.remoteHub",
            "overview": "Remotely browse and edit any GitHub repository. Seamlessly work with code stored on GitHub.",
            "tags": ["github", "remote", "repository", "git"]
        },
        {
            "name": "GitHub Copilot",
            "id": "GitHub.copilot",
            "overview": "GitHub Copilot is an AI-powered code completion tool that helps you write code faster by suggesting whole lines or blocks of code.",
            "tags": ["ai", "code-completion", "github", "productivity"]
        },
        {
            "name": "GitHub Copilot Chat",
            "id": "GitHub.copilot-chat",
            "overview": "GitHub Copilot Chat is an AI-powered chat interface that helps you code faster and with more confidence.",
            "tags": ["ai", "chat", "github", "productivity"]
        },
        {
            "name": "GitLens — Git supercharged",
            "id": "eamodio.gitlens",
            "overview": "GitLens supercharges the built-in VS Code Git capabilities, providing rich insights into code authorship, history, and more, right in your editor.",
            "tags": ["git", "version-control", "history", "blame"]
        }
    ],
    
    "Web Development": [
        {
            "name": "Live Server",
            "id": "ritwickdey.LiveServer",
            "overview": "Live Server launches a local development server with live reload for static and dynamic pages, making web development faster and easier.",
            "tags": ["web-development", "live-reload", "server", "html", "css"]
        },
        {
            "name": "Auto Rename Tag",
            "id": "formulahendry.auto-rename-tag",
            "overview": "Auto Rename Tag automatically renames paired HTML/XML tags, making it easier to edit markup without breaking tag pairs.",
            "tags": ["html", "xml", "web-development", "auto-rename"]
        },
        {
            "name": "CSS Peek",
            "id": "pranaygp.vscode-css-peek",
            "overview": "CSS Peek allows you to peek and go to CSS definitions directly from HTML files, making it easier to navigate between HTML and CSS.",
            "tags": ["css", "html", "web-development", "navigation"]
        },
        {
            "name": "HTML CSS Support",
            "id": "ecmel.vscode-html-css-support",
            "overview": "HTML CSS Support provides CSS class name completion for HTML documents based on definitions in your workspace.",
            "tags": ["html", "css", "autocomplete", "web-development"]
        },
        {
            "name": "Bracket Pair Colorizer",
            "id": "CoenraadS.bracket-pair-colorizer",
            "overview": "Bracket Pair Colorizer allows matching brackets to be identified with colors, making it easier to read and debug code with nested structures.",
            "tags": ["brackets", "syntax-highlighting", "readability", "web-development"]
        },
        {
            "name": "HTML Snippets",
            "id": "abusaidm.html-snippets",
            "overview": "HTML Snippets provides rich language support for HTML, including snippets, syntax highlighting, and more.",
            "tags": ["html", "snippets", "web-development", "productivity"]
        },
        {
            "name": "CSS Formatter",
            "id": "aeschli.vscode-css-formatter",
            "overview": "CSS Formatter formats CSS, SCSS and LESS files. It provides customizable formatting options for your stylesheets.",
            "tags": ["css", "formatter", "scss", "less", "web-development"]
        },
        {
            "name": "HTML to CSS autocompletion",
            "id": "solnurkarim.html-to-css-autocompletion",
            "overview": "HTML to CSS autocompletion provides CSS class name suggestions based on HTML structure and existing CSS classes.",
            "tags": ["html", "css", "autocomplete", "web-development"]
        },
        {
            "name": "Live Sass Compiler",
            "id": "ritwickdey.live-sass",
            "overview": "Live Sass Compiler watches your Sass/SCSS files and compiles them to CSS files in real-time with live reload.",
            "tags": ["sass", "scss", "css", "compiler", "web-development"]
        },
        {
            "name": "Web Accessibility",
            "id": "maxvanderschee.web-accessibility",
            "overview": "Web Accessibility helps you create accessible web applications by providing linting and suggestions for accessibility issues.",
            "tags": ["accessibility", "web-development", "a11y", "linting"]
        }
    ],
    
    "JavaScript & TypeScript": [
        {
            "name": "JavaScript (ES6) code snippets",
            "id": "xabikos.JavaScriptSnippets",
            "overview": "This extension contains code snippets for JavaScript in ES6 syntax for VS Code editor.",
            "tags": ["javascript", "snippets", "es6", "productivity"]
        },
        {
            "name": "TypeScript Importer",
            "id": "pmneo.tsimporter",
            "overview": "TypeScript Importer automatically searches for TypeScript definitions in workspace files and provides all available imports.",
            "tags": ["typescript", "imports", "autocomplete", "productivity"]
        },
        {
            "name": "Import Cost",
            "id": "wix.vscode-import-cost",
            "overview": "Import Cost displays the size of the imported package above the import statement, helping you optimize your bundle size.",
            "tags": ["javascript", "typescript", "bundle-size", "optimization"]
        },
        {
            "name": "TypeScript Hero",
            "id": "rbbit.typescript-hero",
            "overview": "TypeScript Hero organizes your imports, sorts them and removes unused imports automatically.",
            "tags": ["typescript", "imports", "organization", "productivity"]
        },
        {
            "name": "JavaScript Debugger",
            "id": "ms-vscode.js-debug",
            "overview": "JavaScript Debugger provides debugging support for JavaScript and TypeScript in VS Code.",
            "tags": ["javascript", "typescript", "debugging", "development"]
        },
        {
            "name": "TypeScript Vue Plugin",
            "id": "Vue.volar",
            "overview": "TypeScript Vue Plugin provides TypeScript language support for Vue 3.",
            "tags": ["vue", "typescript", "language-support", "web-development"]
        },
        {
            "name": "JavaScript (ES6) code snippets",
            "id": "xabikos.JavaScriptSnippets",
            "overview": "This extension contains code snippets for JavaScript in ES6 syntax for VS Code editor.",
            "tags": ["javascript", "snippets", "es6", "productivity"]
        },
        {
            "name": "TypeScript Vue Plugin",
            "id": "Vue.volar",
            "overview": "TypeScript Vue Plugin provides TypeScript language support for Vue 3.",
            "tags": ["vue", "typescript", "language-support", "web-development"]
        },
        {
            "name": "JavaScript (ES6) code snippets",
            "id": "xabikos.JavaScriptSnippets",
            "overview": "This extension contains code snippets for JavaScript in ES6 syntax for VS Code editor.",
            "tags": ["javascript", "snippets", "es6", "productivity"]
        },
        {
            "name": "TypeScript Vue Plugin",
            "id": "Vue.volar",
            "overview": "TypeScript Vue Plugin provides TypeScript language support for Vue 3.",
            "tags": ["vue", "typescript", "language-support", "web-development"]
        }
    ],
    
    "Python Development": [
        {
            "name": "Python",
            "id": "ms-python.python",
            "overview": "The Python extension provides rich support for the Python language, including features such as IntelliSense, linting, debugging, code navigation, code formatting, refactoring, variable explorer, test explorer, and more.",
            "tags": ["python", "intellisense", "debugging", "linting"]
        },
        {
            "name": "Pylance",
            "id": "ms-python.vscode-pylance",
            "overview": "Pylance is a fast, feature-rich language server for Python in VS Code, providing type checking, auto-imports, and more.",
            "tags": ["python", "type-checking", "language-server", "intellisense"]
        },
        {
            "name": "Python Docstring Generator",
            "id": "njpwerner.autodocstring",
            "overview": "Generates docstrings for Python functions automatically, supporting Google, NumPy, and Sphinx formats.",
            "tags": ["python", "documentation", "docstrings", "productivity"]
        },
        {
            "name": "Python Indent",
            "id": "KevinRose.vscode-python-indent",
            "overview": "Python Indent provides correct indentation for Python code, making it easier to write properly formatted Python code.",
            "tags": ["python", "indentation", "formatting", "productivity"]
        },
        {
            "name": "Python Type Hint",
            "id": "njpwerner.autodocstring",
            "overview": "Python Type Hint provides type checking and IntelliSense for Python type hints.",
            "tags": ["python", "type-hints", "intellisense", "productivity"]
        },
        {
            "name": "Python Test Explorer",
            "id": "LittleFoxTeam.vscode-python-test-adapter",
            "overview": "Python Test Explorer provides a test explorer for Python tests, making it easy to run and debug tests.",
            "tags": ["python", "testing", "test-explorer", "productivity"]
        },
        {
            "name": "Python Environment Manager",
            "id": "donjayamanne.python-environment-manager",
            "overview": "Python Environment Manager helps you manage Python environments and virtual environments in VS Code.",
            "tags": ["python", "environments", "virtual-env", "productivity"]
        },
        {
            "name": "Python Path",
            "id": "ms-python.python",
            "overview": "Python Path helps you manage Python paths and environments in VS Code.",
            "tags": ["python", "paths", "environments", "productivity"]
        },
        {
            "name": "Python Snippets",
            "id": "ms-python.python",
            "overview": "Python Snippets provides code snippets for Python development in VS Code.",
            "tags": ["python", "snippets", "productivity", "development"]
        },
        {
            "name": "Python Interactive",
            "id": "ms-python.python",
            "overview": "Python Interactive provides an interactive Python console in VS Code for testing and debugging.",
            "tags": ["python", "interactive", "console", "debugging"]
        }
    ],
    
    "Database & SQL": [
        {
            "name": "SQLTools",
            "id": "mtxr.sqltools",
            "overview": "SQLTools is a lightweight SQL client with a clean interface, supporting multiple databases and providing syntax highlighting and autocomplete.",
            "tags": ["sql", "database", "query", "client"]
        },
        {
            "name": "SQL Server (mssql)",
            "id": "ms-mssql.mssql",
            "overview": "Microsoft SQL Server extension for VS Code, providing IntelliSense, debugging, and query execution capabilities.",
            "tags": ["sql", "mssql", "database", "microsoft"]
        },
        {
            "name": "PostgreSQL",
            "id": "ckolkman.vscode-postgres",
            "overview": "PostgreSQL extension for VS Code provides IntelliSense, debugging, and query execution for PostgreSQL databases.",
            "tags": ["sql", "postgresql", "database", "intellisense"]
        },
        {
            "name": "MySQL",
            "id": "cweijan.vscode-mysql-client2",
            "overview": "MySQL extension for VS Code provides IntelliSense, debugging, and query execution for MySQL databases.",
            "tags": ["sql", "mysql", "database", "intellisense"]
        },
        {
            "name": "SQLite",
            "id": "qwtel.sqlite-viewer",
            "overview": "SQLite extension for VS Code provides IntelliSense, debugging, and query execution for SQLite databases.",
            "tags": ["sql", "sqlite", "database", "intellisense"]
        },
        {
            "name": "MongoDB for VS Code",
            "id": "mongodb.mongodb-vscode",
            "overview": "MongoDB for VS Code provides IntelliSense, debugging, and query execution for MongoDB databases.",
            "tags": ["mongodb", "database", "nosql", "intellisense"]
        },
        {
            "name": "Redis",
            "id": "cweijan.vscode-redis-client",
            "overview": "Redis extension for VS Code provides IntelliSense, debugging, and query execution for Redis databases.",
            "tags": ["redis", "database", "nosql", "intellisense"]
        },
        {
            "name": "Cassandra",
            "id": "ms-mssql.mssql",
            "overview": "Cassandra extension for VS Code provides IntelliSense, debugging, and query execution for Cassandra databases.",
            "tags": ["cassandra", "database", "nosql", "intellisense"]
        },
        {
            "name": "Elasticsearch",
            "id": "ms-mssql.mssql",
            "overview": "Elasticsearch extension for VS Code provides IntelliSense, debugging, and query execution for Elasticsearch databases.",
            "tags": ["elasticsearch", "database", "nosql", "intellisense"]
        },
        {
            "name": "Neo4j",
            "id": "ms-mssql.mssql",
            "overview": "Neo4j extension for VS Code provides IntelliSense, debugging, and query execution for Neo4j graph databases.",
            "tags": ["neo4j", "database", "graph", "intellisense"]
        }
    ],
    
    "Productivity & Navigation": [
        {
            "name": "Path Intellisense",
            "id": "christian-kohler.path-intellisense",
            "overview": "Path Intellisense autocompletes filenames in your code, making it easier to import files and navigate your project.",
            "tags": ["navigation", "autocomplete", "file-paths", "productivity"]
        },
        {
            "name": "Auto Import",
            "id": "steoates.autoimport",
            "overview": "Auto Import automatically finds, parses and provides code actions for all available imports, making it easier to manage imports.",
            "tags": ["imports", "autocomplete", "productivity", "typescript"]
        },
        {
            "name": "Bookmarks",
            "id": "alefragnani.Bookmarks",
            "overview": "Bookmarks helps you navigate in your code, moving between important positions easily and quickly.",
            "tags": ["navigation", "bookmarks", "productivity", "code-navigation"]
        },
        {
            "name": "Bracket Pair Colorizer",
            "id": "CoenraadS.bracket-pair-colorizer",
            "overview": "Bracket Pair Colorizer allows matching brackets to be identified with colors, making it easier to read and debug code with nested structures.",
            "tags": ["brackets", "syntax-highlighting", "readability", "productivity"]
        },
        {
            "name": "Code Spell Checker",
            "id": "streetsidesoftware.code-spell-checker",
            "overview": "Code Spell Checker is a basic spell checker that works well with code and documents, helping you catch common spelling errors.",
            "tags": ["spell-check", "documentation", "comments", "productivity"]
        },
        {
            "name": "Error Lens",
            "id": "usernamehw.errorlens",
            "overview": "Error Lens improves the visibility of errors and warnings in your code by showing them inline.",
            "tags": ["errors", "warnings", "visibility", "productivity"]
        },
        {
            "name": "Todo Tree",
            "id": "Gruntfuggly.todo-tree",
            "overview": "Todo Tree highlights TODO, FIXME, and other annotations within your code, making them easy to find and track.",
            "tags": ["todo", "annotations", "tracking", "productivity"]
        },
        {
            "name": "Indent Rainbow",
            "id": "oderwat.indent-rainbow",
            "overview": "Indent Rainbow makes indentation easier to read by coloring each indentation level with a different color.",
            "tags": ["indentation", "readability", "syntax-highlighting", "productivity"]
        },
        {
            "name": "Trailing Spaces",
            "id": "shardulm94.trailing-spaces",
            "overview": "Trailing Spaces highlights trailing spaces and deletes them on save, keeping your code clean.",
            "tags": ["trailing-spaces", "cleanup", "formatting", "productivity"]
        },
        {
            "name": "Word Count",
            "id": "ms-vscode.wordcount",
            "overview": "Word Count displays the word count for the current file in the status bar, useful for documentation and writing.",
            "tags": ["word-count", "documentation", "writing", "productivity"]
        }
    ],
    
    "Themes & Icons": [
        {
            "name": "Material Icon Theme",
            "id": "PKief.material-icon-theme",
            "overview": "Material Icon Theme provides beautiful icons for VS Code, making it easier to identify file types and navigate your project.",
            "tags": ["icons", "material-design", "file-explorer", "visual"]
        },
        {
            "name": "One Dark Pro",
            "id": "zhuangtongfa.Material-theme",
            "overview": "One Dark Pro is a beautiful dark theme for VS Code, inspired by Atom's One Dark theme.",
            "tags": ["theme", "dark", "one-dark", "visual"]
        },
        {
            "name": "Dracula Official",
            "id": "dracula-theme.theme-dracula",
            "overview": "Dracula is a dark theme for VS Code and many other applications, featuring a carefully selected color palette.",
            "tags": ["theme", "dark", "dracula", "visual"]
        },
        {
            "name": "Night Owl",
            "id": "sdras.night-owl",
            "overview": "Night Owl is a VS Code theme for the night owls out there. Working late again? This theme is for you.",
            "tags": ["theme", "dark", "night", "visual"]
        },
        {
            "name": "Monokai Pro",
            "id": "monokai.theme-monokai-pro-vscode",
            "overview": "Monokai Pro is a beautiful theme with carefully selected colors for a great coding experience.",
            "tags": ["theme", "dark", "monokai", "visual"]
        },
        {
            "name": "GitHub Theme",
            "id": "GitHub.github-vscode-theme",
            "overview": "GitHub Theme provides light and dark themes that match GitHub's design system.",
            "tags": ["theme", "github", "light", "dark", "visual"]
        },
        {
            "name": "Ayu",
            "id": "teabyii.ayu",
            "overview": "Ayu is a simple theme with bright colors and comes in three versions — dark, light and mirage for all day long comfortable coding.",
            "tags": ["theme", "ayu", "comfortable", "visual"]
        },
        {
            "name": "Palenight Theme",
            "id": "whizkydee.material-palenight-theme",
            "overview": "Palenight Theme is an elegant and juicy material-like theme for VS Code.",
            "tags": ["theme", "dark", "material", "visual"]
        },
        {
            "name": "Winter is Coming",
            "id": "johnpapa.winteriscoming",
            "overview": "Winter is Coming is a collection of beautiful themes for VS Code with a focus on readability and aesthetics.",
            "tags": ["theme", "winter", "beautiful", "visual"]
        },
        {
            "name": "Tokyo Night",
            "id": "enkia.tokyo-night",
            "overview": "Tokyo Night is a clean, dark theme that aims to create a calm feeling, with colors that are easy on the eyes.",
            "tags": ["theme", "dark", "tokyo", "calm", "visual"]
        }
    ],
    
    "Testing & Debugging": [
        {
            "name": "Debugger for Chrome",
            "id": "msjsdiag.debugger-for-chrome",
            "overview": "Debugger for Chrome enables you to debug your JavaScript code running in Google Chrome directly from VS Code.",
            "tags": ["debugging", "chrome", "javascript", "web-development"]
        },
        {
            "name": "Jest",
            "id": "Orta.vscode-jest",
            "overview": "Jest extension for VS Code provides a comprehensive testing experience with Jest, including test discovery, running, and debugging.",
            "tags": ["testing", "jest", "javascript", "unit-tests"]
        },
        {
            "name": "Thunder Client",
            "id": "rangav.vscode-thunder-client",
            "overview": "Thunder Client is a lightweight REST API client for VS Code, allowing you to test APIs directly from your editor.",
            "tags": ["api", "rest", "testing", "http-client"]
        },
        {
            "name": "REST Client",
            "id": "humao.rest-client",
            "overview": "REST Client allows you to send HTTP requests and view the response in VS Code directly.",
            "tags": ["api", "rest", "http", "testing"]
        },
        {
            "name": "Postman",
            "id": "Postman.postman-code-generators",
            "overview": "Postman Code Generators allows you to generate code snippets for various languages from your Postman requests.",
            "tags": ["postman", "api", "code-generation", "testing"]
        },
        {
            "name": "Cucumber (Gherkin)",
            "id": "CucumberOpen.cucumber-official",
            "overview": "Cucumber (Gherkin) provides syntax highlighting and IntelliSense for Gherkin feature files.",
            "tags": ["cucumber", "gherkin", "bdd", "testing"]
        },
        {
            "name": "Test Explorer UI",
            "id": "hbenl.vscode-test-explorer",
            "overview": "Test Explorer UI provides a test explorer for various testing frameworks in VS Code.",
            "tags": ["testing", "test-explorer", "ui", "productivity"]
        },
        {
            "name": "Coverage Gutters",
            "id": "ryanluker.vscode-coverage-gutters",
            "overview": "Coverage Gutters displays code coverage information in the gutter, making it easy to see which lines are covered by tests.",
            "tags": ["coverage", "testing", "gutter", "productivity"]
        },
        {
            "name": "Debug Visualizer",
            "id": "hediet.vscode-debug-visualizer",
            "overview": "Debug Visualizer helps you visualize data structures while debugging, making it easier to understand complex data.",
            "tags": ["debugging", "visualization", "data-structures", "productivity"]
        },
        {
            "name": "Error Lens",
            "id": "usernamehw.errorlens",
            "overview": "Error Lens improves the visibility of errors and warnings in your code by showing them inline.",
            "tags": ["errors", "warnings", "visibility", "debugging"]
        }
    ],
    
    "Docker & DevOps": [
        {
            "name": "Docker",
            "id": "ms-azuretools.vscode-docker",
            "overview": "The Docker extension makes it easy to build, manage and deploy containerized applications from VS Code.",
            "tags": ["docker", "containers", "devops", "deployment"]
        },
        {
            "name": "Remote - SSH",
            "id": "ms-vscode-remote.remote-ssh",
            "overview": "Remote - SSH allows you to open a folder on a remote machine using SSH, making it easy to develop on remote servers.",
            "tags": ["ssh", "remote", "devops", "server"]
        },
        {
            "name": "YAML",
            "id": "redhat.vscode-yaml",
            "overview": "YAML language support for VS Code, providing syntax highlighting, validation, and formatting for YAML files.",
            "tags": ["yaml", "configuration", "devops", "kubernetes"]
        },
        {
            "name": "Kubernetes",
            "id": "ms-kubernetes-tools.vscode-kubernetes-tools",
            "overview": "Kubernetes extension for VS Code provides IntelliSense, debugging, and deployment capabilities for Kubernetes.",
            "tags": ["kubernetes", "containers", "devops", "deployment"]
        },
        {
            "name": "Azure Tools",
            "id": "ms-vscode.vscode-azureextensionpack",
            "overview": "Azure Tools provides extensions for working with Azure services directly from VS Code.",
            "tags": ["azure", "cloud", "devops", "microsoft"]
        },
        {
            "name": "AWS Toolkit",
            "id": "AmazonWebServices.aws-toolkit-vscode",
            "overview": "AWS Toolkit provides extensions for working with AWS services directly from VS Code.",
            "tags": ["aws", "cloud", "devops", "amazon"]
        },
        {
            "name": "Google Cloud Code",
            "id": "GoogleCloudTools.cloudcode",
            "overview": "Google Cloud Code provides extensions for working with Google Cloud services directly from VS Code.",
            "tags": ["google-cloud", "cloud", "devops", "google"]
        },
        {
            "name": "Terraform",
            "id": "hashicorp.terraform",
            "overview": "Terraform extension for VS Code provides IntelliSense, debugging, and deployment capabilities for Terraform.",
            "tags": ["terraform", "iac", "devops", "infrastructure"]
        },
        {
            "name": "Ansible",
            "id": "redhat.vscode-ansible",
            "overview": "Ansible extension for VS Code provides IntelliSense, debugging, and deployment capabilities for Ansible.",
            "tags": ["ansible", "automation", "devops", "configuration"]
        },
        {
            "name": "Jenkins",
            "id": "ms-vscode.vscode-azureextensionpack",
            "overview": "Jenkins extension for VS Code provides integration with Jenkins CI/CD pipelines.",
            "tags": ["jenkins", "ci-cd", "devops", "automation"]
        }
    ],
    
    "AI & Code Assistance": [
        {
            "name": "GitHub Copilot",
            "id": "GitHub.copilot",
            "overview": "GitHub Copilot is an AI-powered code completion tool that helps you write code faster by suggesting whole lines or blocks of code.",
            "tags": ["ai", "code-completion", "productivity", "github"]
        },
        {
            "name": "Tabnine AI Autocomplete",
            "id": "tabnine.tabnine-vscode",
            "overview": "Tabnine is an AI code completion tool that helps you code faster with intelligent suggestions based on your coding patterns.",
            "tags": ["ai", "autocomplete", "productivity", "code-completion"]
        },
        {
            "name": "IntelliCode",
            "id": "VisualStudioExptTeam.vscodeintellicode",
            "overview": "IntelliCode provides AI-assisted development features for Python, TypeScript/JavaScript and Java developers in Visual Studio Code.",
            "tags": ["ai", "intellisense", "productivity", "microsoft"]
        },
        {
            "name": "Kite",
            "id": "kiteco.kite",
            "overview": "Kite is an AI-powered coding assistant that provides intelligent code completions and documentation.",
            "tags": ["ai", "code-completion", "documentation", "productivity"]
        },
        {
            "name": "CodeGPT",
            "id": "DanielSanMedium.dscodegpt",
            "overview": "CodeGPT is an AI-powered coding assistant that helps you write, debug, and explain code.",
            "tags": ["ai", "code-assistant", "debugging", "productivity"]
        },
        {
            "name": "CodeWhisperer",
            "id": "AmazonWebServices.aws-toolkit-vscode",
            "overview": "CodeWhisperer is an AI-powered coding assistant that provides intelligent code completions and suggestions.",
            "tags": ["ai", "code-completion", "aws", "productivity"]
        },
        {
            "name": "Claude",
            "id": "anthropic.claude",
            "overview": "Claude is an AI assistant that helps you write, debug, and explain code with natural language conversations.",
            "tags": ["ai", "assistant", "conversation", "productivity"]
        },
        {
            "name": "Codeium",
            "id": "Exafunction.codeium",
            "overview": "Codeium is an AI-powered code completion tool that provides intelligent suggestions based on your codebase.",
            "tags": ["ai", "code-completion", "intelligent", "productivity"]
        },
        {
            "name": "Replit Ghostwriter",
            "id": "replit.replit",
            "overview": "Replit Ghostwriter is an AI-powered coding assistant that helps you write, debug, and explain code.",
            "tags": ["ai", "coding-assistant", "debugging", "productivity"]
        },
        {
            "name": "CodeT5",
            "id": "Salesforce.code-t5",
            "overview": "CodeT5 is an AI-powered code completion and generation tool that helps you write code faster.",
            "tags": ["ai", "code-generation", "completion", "productivity"]
        }
    ]
}

# Flatten all extensions into a single list
all_extensions = []
for category, extensions in extensions_by_category.items():
    for ext in extensions:
        ext["category"] = category
        all_extensions.append(ext)

today = datetime.now().strftime("%Y-%m-%d")
ext_dir = "extensions"
used_ids = set()

# Scan all markdown files in the extensions directory for used IDs
if os.path.exists(ext_dir):
    for fname in os.listdir(ext_dir):
        if fname.endswith(".md"):
            with open(os.path.join(ext_dir, fname), "r", encoding="utf-8") as f:
                for line in f:
                    match = re.match(r"\\*\\*ID:\\*\\* `([^`]+)`", line)
                    if match:
                        used_ids.add(match.group(1))

# Filter out used extensions
unused_extensions = [ext for ext in all_extensions if ext["id"] not in used_ids]

if not unused_extensions:
    print("All extensions have been used! No new extension to add.")
    exit(0)

chosen = random.choice(unused_extensions)
url = f"https://marketplace.visualstudio.com/items?itemName={chosen['id']}"

# Create SEO-friendly content with structured data
md = f"""# VS Code Extension of the Day - {today}

**Name:** {chosen['name']}  
**Category:** {chosen['category']}  
**Marketplace Link:** [View Extension]({url})  
**ID:** `{chosen['id']}`  
**Overview:** {chosen['overview']}  

## Tags
{', '.join([f'`{tag}`' for tag in chosen['tags']])}

## Why This Extension?

This extension is particularly useful for developers working with {', '.join(chosen['tags'][:3])}. It helps improve your development workflow by {chosen['overview'].lower().split('.')[0]}.

## Installation

1. Open VS Code
2. Press `Ctrl+Shift+X` to open the Extensions view
3. Search for "{chosen['name']}"
4. Click **Install**

## Related Extensions

Looking for more extensions in the **{chosen['category']}** category? Check out our other recommendations for similar tools and utilities.

---

*This extension was automatically selected from our curated list of the best VS Code extensions for developers. Each day, we feature a different extension to help you discover new tools that can improve your coding experience.*
"""

os.makedirs(ext_dir, exist_ok=True)
with open(f"{ext_dir}/{today}.md", "w", encoding="utf-8") as f:
    f.write(md)

print(f"Generated extension entry for {today}: {chosen['name']}")
print(f"Category: {chosen['category']}")
print(f"Tags: {', '.join(chosen['tags'])}") 