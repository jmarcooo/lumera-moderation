import re

with open('packages.html', 'r') as f:
    content = f.read()

# Let's replace the whole decision block styling
css_search = """        /* --- STYLED DECISION BUTTONS --- */
        .dp-title { font-size: 14px; font-weight: 600; color: var(--text-main); margin-bottom: 12px; }
        .decision-wrapper { display: flex; flex-direction: column; width: 100%; }
        .decision-group { display: flex; flex-direction: column; gap: 8px; }

        .decision-label { flex: 1; display: flex; align-items: center; gap: 8px; padding: 10px 14px; border: 1px solid var(--border-color); border-radius: 6px; font-size: 13px; font-weight: 500; cursor: pointer; transition: all 0.2s; user-select: none; background-color: #ffffff; }
        .decision-label input[type="radio"] { display: none; }

        .decision-label.approve:hover { border-color: var(--text-main); background-color: #f3f4f6; }
        .decision-label.reject:hover { border-color: var(--color-reject); background-color: #fef2f2; }

        /* Checked States */
        .decision-label:has(input[value="approve"]:checked) { background-color: #e5e7eb; border-color: var(--text-main); color: var(--text-main); font-weight: 600; }
        .decision-label:has(input[value="reject"]:checked) { background-color: var(--bg-reject); border-color: var(--color-reject); color: var(--color-reject); font-weight: 600; }

        .rejection-reason { display: none; margin-top: 12px; animation: fadeIn 0.2s ease-in-out; }
        .decision-wrapper:has(input[value="reject"]:checked) .rejection-reason { display: block; }
        .rejection-reason select { width: 100%; padding: 10px 12px; border-radius: 6px; border: 1px solid var(--border-color); font-size: 13px; color: var(--text-main); background-color: #ffffff; outline: none; cursor: pointer; }
        .rejection-reason select:focus { border-color: #8b5cf6; box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.2); }"""

css_replace = """        /* --- RADIO DECISION STYLING (Profile Style) --- */
        .dp-title { font-size: 14px; font-weight: 600; color: var(--text-main); margin-bottom: 16px; }

        .dp-radio-group { display: flex; flex-direction: column; gap: 10px; }
        .dp-radio-label {
            display: flex; align-items: center; gap: 8px;
            font-size: 13px; font-weight: 500; color: var(--text-main);
            cursor: pointer; padding: 4px 0;
        }
        .dp-radio-label input[type="radio"] {
            accent-color: #8b5cf6;
            width: 16px; height: 16px;
            cursor: pointer;
        }

        .dp-sub-reasons {
            display: none;
            flex-direction: column;
            gap: 8px;
            margin-top: 12px;
            background: #fff1f2;
            padding: 12px;
            border-radius: 6px;
            border: 1px solid #ffe4e6;
        }

        .dp-sub-reasons .dp-radio-label { color: #881337; font-weight: 400; }
        .dp-sub-reasons .dp-radio-label input[type="radio"] { accent-color: #e11d48; }

        /* Reveal sub-reasons when reject is checked */
        .block-decision:has(input[value="reject"]:checked) .dp-sub-reasons {
            display: flex;
        }"""

if css_search in content:
    content = content.replace(css_search, css_replace)
else:
    print("CSS search block not found, trying fallback...")

with open('packages.html', 'w') as f:
    f.write(content)
