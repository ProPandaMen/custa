# 🚀 Custa

**Custa** is a custom markup-based static site generator that lets you build clean, minimal HTML websites using your own syntax.
Write readable `.kms` files with intuitive tags like `@section`, `@button`, or `@fetch` — and generate fully styled HTML pages.

---

## 🗺️ Roadmap

- [x] Project structure initialized
- [ ] CLI interface and base commands created (`build`, `new`, `serve`)
- [ ] Basic rendering logic implemented
- [ ] Support for custom tags (e.g. `@button`, `@section`)
- [ ] Add support for nested blocks (`@for`, `@if`)
- [ ] HTTP fetch integration (`@fetch`)
- [ ] Markdown support inside sections
- [ ] Theming and template system
- [ ] Plugin architecture

---

## 💻 CLI Commands

> All commands are executed using:
> ```bash
> python -m custa.cli [command]
> ```

### 🔨 `custa build`
Builds all `.kms` files from the `content/` folder into `.html` files in the `output/` folder.

### 📝 `custa new [filename]`
Creates a new `.kms` file with starter content in the `content/` folder.

### 🌐 `custa serve`
Launches a local development server to preview the generated site from the `output/` folder.

---

## 🙋‍♂️ Author

Built with ❤️ by **ProPandaMen**

