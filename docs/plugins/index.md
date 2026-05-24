---
title: Plugins
image:
---

Quartz's functionality is provided by a collection of first-party community plugins. Each plugin can be enabled, disabled, and configured via `quartz.config.yaml`. See [[configuration#Plugins|Configuration]] for details on how to manage plugins.

> [!info] Internal vs Community Plugins
> Quartz has two kinds of plugins:
>
> - **Community plugins** are standalone repositories under [`quartz-community`](https://github.com/quartz-community). In TS overrides, they use `ExternalPlugin.X()` (imported from `.quartz/plugins`).
> - **Internal plugins** are built into Quartz core (Assets, Static, ComponentResources, NotFoundPage). In TS overrides, they use `Plugin.X()` (imported from `./quartz/plugins`).

## Plugin types

Quartz plugins fall into several categories:

- **Transformers** process content during the build, e.g. parsing frontmatter, highlighting syntax, or resolving links.
- **Filters** decide which content files to include or exclude from the output.
- **Page Types** generate HTML pages — one per content file, folder, tag, canvas, or bases view.
- **Components** render UI elements in the page layout (sidebars, headers, footers, etc.).

## First-party plugins

![[Plugins.base]]

> [!note] Multi-category plugins
> Some plugins span multiple categories. **TableOfContents** is both a transformer and a component. **EncryptedPages** is a transformer, emitter, and component. They appear in each relevant category above.
