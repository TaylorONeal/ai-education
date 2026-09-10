# Install, use, and update

Choose one route. Installation is optional. This toolkit contains instructions and templates, not an AI model or an LMS connection.

## 1. Any AI chat: copy and paste

Download the repository, open `web/dist/index.html`, choose a task, and copy its prompt. Paste it into your approved AI chat and fill the placeholders there. No terminal, API key, or installer is needed. You can also read the skill directly under `skills/`.

If your chat cannot fetch links, paste the text or attach the file. Never claim the skill is installed just because the AI says it understands the prompt.

## 2. A product with skill uploads

In the visual guide, download the selected skill as a ZIP. Use your product's custom-skill upload if available. Each ZIP contains one named folder with `SKILL.md`, supporting files, and the referenced platform guides. We also generate `.skill` copies for tools that accept that extension. If your product rejects `.skill`, use the ZIP; menus and upload support vary by account.

Claude documents ZIP skill uploads in its [official help](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Follow the current product screen rather than assuming a fixed menu path. This repository is not a published marketplace plugin.

## 3. Local agents: preview, then install

Download and extract the repository, or clone it. Open a terminal in the repository folder. Python 3.9 or newer is required for packaging and installation.

```sh
python3 scripts/install.py --agent codex --skill start-here --dry-run
python3 scripts/install.py --agent codex --skill start-here
```

On Windows, use `py -3` in place of `python3`. PowerShell users can run the same Python arguments. The shell wrapper `bash scripts/install.sh` remains available on macOS/Linux and defaults to Claude for backward compatibility.

| Agent target | Personal destination | Project destination |
|---|---|---|
| `codex` or `agents` | `~/.agents/skills` | `.agents/skills` |
| `claude` | `~/.claude/skills` | `.claude/skills` |
| `gemini` | `~/.gemini/skills` | `.gemini/skills` |
| `copilot` | `~/.copilot/skills` | `.github/skills` |
| `cursor` | `~/.cursor/skills` | `.cursor/skills` |

Use `--project [PROJECT_FOLDER]` for project scope, or `--dest [SKILLS_FOLDER]` for a custom destination. Omit `--skill` to install all fourteen skills; repeat it to select several. Use `--list` to see the available names. Avoid installing the same name in multiple discovery locations.

```sh
python3 scripts/install.py --agent claude --skill announcement-writer --skill quiz-builder --dry-run
python3 scripts/install.py --agent agents --project [PROJECT_FOLDER] --dry-run
```

These directories follow current official documentation: [Codex](https://learn.chatgpt.com/docs/build-skills), [Claude Code](https://code.claude.com/docs/en/skills), [Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/), [Copilot](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference), and [Cursor](https://cursor.com/docs/skills). Checked 2026-09-10. Agent releases and institutional policies can change discovery behavior.

## Verify discovery and use

Ask the agent to list the installed skills and open `start-here/SKILL.md`. Verify the actual file, not only its answer. Then say: "Use start-here to help me choose one teaching task."

Codex CLI supports `/skills` and `$skill-name`; Claude Code supports `/skill-name`; Gemini CLI has `/skills list` and `/skills reload`; Cursor provides its skill picker. See the official links above for your exact product surface. Restart if a new directory is not detected. Cloud agents need the files in their own checkout or supported distribution; a personal install on your laptop does not travel automatically.

## Updates preserve your existing copy

Obtain the updated repository, preview the install, then run it again. Identical skills are skipped. Changed skill folders are moved to a timestamped sibling backup directory outside skill discovery before replacements are installed. The installer prints each backup location. It refuses a symlink destination and does not merge your custom edits into upstream files.

To restore, close the agent, move the new skill folder aside, then move the saved folder back to its original location. Keep personal variations under a different skill name to avoid collisions. Uninstall by moving only this toolkit's named skill folders out of the discovery directory; do not delete other skills.

## Repository-reading, browser, and custom agents

No native skill support? Give the agent the repository or a selected ZIP and instruct it to read `SKILL.md` plus the referenced files. If it has no file tools, paste the relevant instructions. See [all agent types](guides/agents.md), including headless and scheduled runs.

## Troubleshooting

| Problem | Next step |
|---|---|
| Python is missing | Use copy-paste or ZIP upload; technical users can install Python 3 |
| Skill does not appear | Check the destination and exact `name/SKILL.md` structure; refresh/restart |
| Referenced guide cannot be read | Reinstall a generated portable package, not a bare copied skill folder |
| LMS retrieval fails | Verify connection, course scope, and permissions; use an approved export |
| A download link fails | Rebuild with `python3 scripts/build-toolkit.py`, or obtain a complete release |
| Browser copy is blocked | Select the visible prompt and copy it manually |
