**CICD** https://youtu.be/mFFXuXjVgkU?si=gFjr1G0jfO8FxBuT (checkout the video)

- continuous integration and continuos delivery(deployment).
- It helps developers focus more on code itself.
- We right the github actions or workflows which one of them is the CICD pipeline. There are more workflows.
- The CICD workflow is written on a file called YAML (data-serialization format) files. It is is a text file that used to be named. <Yet Another Markup Language> but it was changed to show that it is not a markup language to <YAML Ain’t Markup Language>.
- A YAML file has these 5 things: Events (when the workflow runs), Jobs (groups of work), Runners (the runner/VM), Steps (individual commands or actions) and Actions (reusable steps via uses:).
  - Sample YAML with the 5 things:

```YAML
name: CI Pipeline

# ┌───────────────────────────────┐
# │ 1. Event                      │
# └───────────────────────────────┘
on:                           # ←── Event trigger
  push:                       # ←── “push” is the event type
    branches:
      - main

# ┌───────────────────────────────┐
# │ 2. Jobs                       │
# └───────────────────────────────┘
jobs:                         # ←── Defines one or more jobs
  build:                      # ←── Job name
    # ┌───────────────────────────┐
    # │ 3. Runner                 │
    # └───────────────────────────┘
    runs-on: ubuntu-latest    # ←── Which VM image to use

    # ┌───────────────────────────┐
    # │ 4. Steps                   │
    # └───────────────────────────┘
    steps:                     # ←── Ordered list of steps
      - name: Checkout code
        # ┌───────────────────────┐
        # │ 5. Action              │
        # └───────────────────────┘
        uses: actions/checkout@v3  # ←── A pre-built action

      - name: Setup Node.js
        uses: actions/setup-node@v3  # ←── Another action
        with:
          node-version: 18

      - name: Install dependencies
        run: npm ci               # ←── A plain shell command

      - name: Run tests
        run: npm test             # ←── Another shell command

```

- In order to add the workflow it has to follow certain requirements.
  - The requirements are:
  1. create a repository or go to the one that exists.
  2. Select add file -> create new file.
  3. We need to be very specific with our naming when we name the file:
     - the proper directory structure should be:
       yourrepo/.github/workflows/thenanyname.yml

# Key characteristics

1. Indentation-based

   - Uses spaces (never tabs) to show hierarchy.
   - Nested items are simply indented under their parent.

2. Data types

   - Scalars: simple values (string, number, true/false).
   - Sequences: ordered lists, marked with dashes (-).
   - Mappings: key/value pairs, like dictionaries or objects.

3. Comments

   - Start with #, and run to the end of the line.

4. File extension
   - Typically .yml or .yaml
