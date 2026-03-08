# reproducible-self-pub-kit

## Source of truth
Canonical workflow, paths, and rules live in **ANCHOR.md**.

If anything disagrees with `ANCHOR.md`, update `ANCHOR.md` first, then fix reality to match.

---

## Git workflow (new user guidance)

### Quick daily commands
~~~powershell
git status -sb
git pull --ff-only
git add -A
git commit -m "Describe your change"
git push
~~~

## W⚓ Protocol
See [W⚓_PROTOCOL.md](W⚓_PROTOCOL.md) for the emergency reset protocol.

---

## Live Implementation

[DoughForge](https://github.com/tonefreqhz/DoughForge) is the active project built using this kit as its foundation.

It demonstrates the full reproducible self-publishing workflow in practice:
- Pandoc-based DOCX, EPUB, and PDF builds
- LuaLaTeX PDF engine with custom preamble
- Git-tracked manuscript and output structure

---

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
