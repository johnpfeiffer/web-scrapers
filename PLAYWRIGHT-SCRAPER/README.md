
# prerequisites

```bash
uv init
uv sync
uv add playwright
uv run playwright install
source .venv/bin/activate
```

# dev

*modify main.py*

`python main.py`

# execute

*for convenience here was the firecrawl way to get all of the links*

`curl -X POST http://localhost:3002/v1/scrape -H 'Content-Type: application/json' -d '{"url": "https://example.com","formats": ["links"]}' > example-links.json`

`for k in $(jq -r '.data.links[]' example-links.json); do echo "$k" >> links.txt; done`

`for k in $(cat links.txt); do python main.py "$k" >> questions-answers.txt; done`

