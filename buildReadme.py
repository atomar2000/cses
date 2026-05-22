from bs4 import BeautifulSoup
from pathlib import Path

HTML_FILE = "cses_page.html"
README_FILE = "README.md"

soup = BeautifulSoup(open(HTML_FILE, encoding="utf-8"), "html.parser")

content = []

content.append("# CSES Problem Set Tracker\n")
content.append("Track progress for solved CSES problems.\n")

# Find all sections
sections = soup.find_all("h2")

for section in sections:
    section_name = section.get_text(strip=True)

    # Skip general section
    if section_name == "General":
        continue

    content.append(f"\n## {section_name}\n")

    ul = section.find_next_sibling("ul")

    if not ul:
        continue

    tasks = ul.find_all("li", class_="task")

    for task in tasks:
        a = task.find("a")

        if not a:
            continue

        title = a.get_text(strip=True)
        href = a["href"]

        full_link = f"https://cses.fi{href}"

        # GitHub markdown checkbox
        content.append(f"- [ ] [{title}]({full_link})")

readme_text = "\n".join(content)

with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(readme_text)

print("README.md generated!")