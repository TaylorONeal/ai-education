# Install

Three ways to use this toolkit, from no install to fully set up. Pick the row that matches you. You can always start at the top and move down later.

| You are | Do this | Setup |
|---|---|---|
| Just want the prompts | Open the [cookbook](cookbook/) or any skill's `SKILL.md`, copy the prompt, paste it into any AI tool | None |
| On Claude Cowork (desktop) | Install the skills as `.skill` bundles, then say "help me get started" | A few clicks |
| On Claude Code or technical | Clone the repo and run the install script, or drop the skills into a project | One command |

After any install, trigger the **start-here** skill (just say "help me get started" or "onboard me") and it walks you through the rest, including pulling in your own course materials.

## Option 1: No install (copy-paste)

Nothing to set up. Open [`cookbook/AI-Teaching-Cookbook.docx`](cookbook/) or any [`skills/<name>/SKILL.md`](skills/), copy the prompt, fill in your bracketed details, and paste it into ChatGPT, Claude, Gemini, or whatever you use. [`GETTING-STARTED.md`](GETTING-STARTED.md) walks through one full task. This is the whole product for most teachers.

## Option 2: Claude Cowork (desktop, no terminal)

Cowork applies installed skills automatically, so once they are in, you just describe what you want and the right skill kicks in. Two ways to get them in.

### The easy way: `.skill` bundles

A `.skill` file is a single packaged skill that Cowork can install with one click.

1. Get the bundles. Download them from the repo's [Releases page](https://github.com/TaylorONeal/ai-education/releases), or build them yourself by running `./scripts/build-bundles.sh` (it writes one `.skill` file per skill into a `dist/` folder).
2. In Cowork, open **Customize** in the left sidebar, then **Settings > Capabilities > Skills**.
3. Click the **+** button and choose **Save skill**, then pick a `.skill` file. Cowork unpacks it into your skills directory automatically.
4. Repeat for each skill you want, or start with just **start-here**, **grading-assistant**, and **announcement-writer** and add more later.
5. Back in a chat, say "help me get started." The start-here skill takes it from there.

### The manual way: copy the folders

If you would rather copy files, put each skill folder into your personal skills directory at `~/.claude/skills/`. Each skill is a folder with a `SKILL.md` inside it, and that structure must be preserved: `~/.claude/skills/grading-assistant/SKILL.md`, not nested any deeper. The install script in Option 3 does exactly this copy for you.

## Option 3: Claude Code, or a clone you control

### One-command install (personal, all skills)

Clone the repo and run the install script. It copies every skill into your personal skills directory (`~/.claude/skills/`), where Claude loads them automatically.

```
git clone https://github.com/TaylorONeal/ai-education.git
cd ai-education
./scripts/install.sh
```

That is it. Open a new session and the skills are available by name. To update later, `git pull` and run the script again.

### Per-project install (shared with a repo)

Claude Code auto-loads skills from a `.claude/skills/` folder at the root of whatever project you are working in, and from any parent directory up to the repo root. To make these skills available inside one of your own projects, copy the skill folders there:

```
mkdir -p /path/to/your/project/.claude/skills
cp -R skills/* /path/to/your/project/.claude/skills/
```

Commit `.claude/skills/` and everyone who clones that project gets the skills too. Note: a `.claude/skills/` folder created mid-session is picked up after you restart the session.

### Pointing an agent at the cloned repo

If you simply hand an agent the cloned repo, it will not auto-install the skills, because they live in `skills/` rather than in a `.claude/skills/` directory. Two clean options: run `./scripts/install.sh` first so the skills are loadable, or tell the agent to read [`AGENTS.md`](AGENTS.md), which is the index of every skill, the guides, and the conventions. With AGENTS.md in context, an agent can follow the skills as instructions even without the auto-load.

## After install: let it onboard you

However you installed, the next step is the same. Trigger the **start-here** skill (say "help me get started"). It asks a few quick questions, offers to pull your course materials in so the other skills are grounded in your real content, and runs your first task end to end. You do not have to read the rest of the repo.

## A one-step bundle for everything (plugins)

Claude's plugin marketplace can package a whole set of skills, connectors, and commands as a single install. If this toolkit is published as a plugin, that becomes the lowest-friction path of all: one install instead of per-skill. Check the [Releases page](https://github.com/TaylorONeal/ai-education/releases) for a plugin build.

## Verify it worked

Start a new session and say "help me get started." If the start-here skill responds by orienting you and asking what you teach, the install took. If nothing happens, confirm the skill folders are at `~/.claude/skills/<name>/SKILL.md` with that exact structure, then restart your session.
