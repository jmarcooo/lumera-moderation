import re

with open('packages.html', 'r') as f:
    content = f.read()

css_search = """        .decision-label.approve:hover { border-color: var(--text-main); background-color: #f3f4f6; }
        .decision-label.reject:hover { border-color: var(--color-reject); background-color: #fef2f2; }

        /* Checked States */
        .decision-label.approve:has(input:checked) { background-color: #10b981; color: white; border-color: #10b981; }
        .decision-label.approve:has(input:checked) i { color: white; }
        .decision-label.reject:has(input:checked) { background-color: var(--color-reject); color: white; border-color: var(--color-reject); }
        .decision-label.reject:has(input:checked) i { color: white; }"""

css_replace = """        /* --- RADIO DECISION STYLING (Profile Style) --- */
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

content = content.replace(css_search, css_replace)

with open('packages.html', 'w') as f:
    f.write(content)
