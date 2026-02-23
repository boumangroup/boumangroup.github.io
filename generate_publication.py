#!/usr/bin/env python3
"""
Generate a YAML snippet for a new publication.
Group members can run this script and send the output to the website maintainer.
"""


def prompt_required(field_name, example=""):
    """Prompt for a required field."""
    while True:
        if example:
            value = input(f"{field_name} (e.g., {example}): ").strip()
        else:
            value = input(f"{field_name}: ").strip()

        if value:
            return value
        print(f"  ⚠️  {field_name} is required. Please try again.")


def prompt_optional(field_name, example=""):
    """Prompt for an optional field."""
    if example:
        value = input(f"{field_name} (optional, e.g., {example}): ").strip()
    else:
        value = input(f"{field_name} (optional): ").strip()
    return value if value else None


def prompt_yes_no(question):
    """Prompt for yes/no question."""
    while True:
        response = input(f"{question} (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        print("  ⚠️  Please enter 'y' or 'n'")


def collect_links():
    """Collect multiple optional links."""
    links = []

    # Always ask for paper link first
    paper_link = prompt_optional("Paper URL", "https://arxiv.org/abs/...")
    if paper_link:
        links.append(('Paper', paper_link, 'orange'))

    # Ask for additional links
    print("\nAdditional links (press Enter to skip):")

    while True:
        link_type = prompt_optional("  Link type", "Project Website, Code, Video")
        if not link_type:
            break

        link_url = prompt_required("  Link URL")
        links.append((link_type, link_url, 'inverse'))

        if not prompt_yes_no("  Add another link?"):
            break

    return links


def generate_yaml_snippet():
    """Generate YAML snippet for a new publication."""
    print("=" * 70)
    print("Generate Publication YAML Snippet - Bouman Group Website")
    print("=" * 70)
    print()

    # Determine publication type
    is_highlight = prompt_yes_no("Is this a highlight publication (shown on homepage)?")
    print()

    # Collect common fields
    title = prompt_required("Title")

    yaml_lines = []

    if is_highlight:
        # Highlight format
        print("\n--- Highlight Publication ---")
        link = prompt_required("Paper/Project URL")
        teaser = prompt_required("Teaser image path", "publications/example.png")

        yaml_lines.append(f'  - title: "{title}"')
        yaml_lines.append(f'    link: "{link}"')
        yaml_lines.append(f'    teaser: "{teaser}"')

        section_name = "highlight"

    else:
        # Regular paper format
        print("\n--- Regular Publication ---")
        authors = prompt_required("Authors", "A. Smith, K.L. Bouman, B. Jones")
        venue = prompt_required("Venue", "CVPR, 2026")

        print()
        links = collect_links()

        yaml_lines.append(f'  - title: "{title}"')
        yaml_lines.append(f'    authors: "{authors}"')
        yaml_lines.append(f'    venue: "{venue}"')

        if links:
            yaml_lines.append('    links:')
            for link_text, link_url, btn_class in links:
                yaml_lines.append(f'      - "[{link_text}]({link_url}){{: .btn .btn--{btn_class}}}"')

        section_name = "papers"

    # Output the YAML snippet
    print("\n" + "=" * 70)
    print(f"YAML SNIPPET TO ADD TO '{section_name}:' SECTION")
    print("=" * 70)
    print()
    print('\n'.join(yaml_lines))
    print()
    print("=" * 70)
    print("\n📋 Copy the above YAML snippet and send it to the website maintainer.")
    print(f"   It should be added at the top of the '{section_name}:' section in")
    print("   _data/publications.yml")
    print()


if __name__ == '__main__':
    try:
        generate_yaml_snippet()
    except KeyboardInterrupt:
        print("\n\n❌ Cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
