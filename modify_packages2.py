import re

with open('packages.html', 'r') as f:
    content = f.read()

# CSS replacement: We need to ensure dp-radio-group and dp-sub-reasons are styled like in verification.html.
css_search = """        .decision-label.approve:hover { border-color: var(--text-main); background-color: #f3f4f6; }
        .decision-label.reject:hover { border-color: var(--color-reject); background-color: #fef2f2; }

        /* Checked States */
        .decision-label.approve:has(input:checked) { background-color: #10b981; color: white; border-color: #10b981; }
        .decision-label.approve:has(input:checked) i { color: white; }
        .decision-label.reject:has(input:checked) { background-color: var(--color-reject); color: white; border-color: var(--color-reject); }
        .decision-label.reject:has(input:checked) i { color: white; }"""

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

content = content.replace(css_search, css_replace)

# Modify html structure for packages.html
html_search = """                            <div class="decision-wrapper">
                                <div class="dp-radio-group">
                                    <label class="dp-radio-label"><input type="radio" name="package_decision" value="approve"> Approve</label>
                                    <label class="dp-radio-label"><input type="radio" name="package_decision" value="reject"> Reject</label>
                                </div>
                                <div class="dp-sub-reasons" style="display: none; margin-top: 10px;">
                                    <select name="package_reject_reason" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid var(--border-color);">
                                        <option value="">Select reason...</option>
                                        <option value="inappropriate">Inappropriate Content</option>
                                        <option value="misleading">Misleading Details</option>
                                    </select>
                                </div>
                            </div>"""

html_replace = """                            <div class="dp-radio-group">
                                <label class="dp-radio-label"><input type="radio" name="package_decision" value="approve"> Approve</label>
                                <label class="dp-radio-label"><input type="radio" name="package_decision" value="reject"> Reject</label>
                            </div>
                            <div class="dp-sub-reasons">
                                <label class="dp-radio-label"><input type="radio" name="r_package_reason" value="inappropriate"> Inappropriate Content</label>
                                <label class="dp-radio-label"><input type="radio" name="r_package_reason" value="misleading"> Misleading Details</label>
                                <label class="dp-radio-label"><input type="radio" name="r_package_reason" value="offensive"> Offensive Language</label>
                                <label class="dp-radio-label"><input type="radio" name="r_package_reason" value="unrealistic"> Unrealistic Expectations</label>
                            </div>
                            <div style="margin-top: 12px;">
                                <label style="font-size: 13px; font-weight: 600; color: var(--text-main); margin-bottom: 4px; display: block;">Moderator Input / Insights (Optional)</label>
                                <textarea name="moderator_insights" rows="3" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid var(--border-color); resize: vertical; font-size: 13px; font-family: inherit;"></textarea>
                            </div>"""

content = content.replace(html_search, html_replace)

js_search = """        // Show reason dropdown when Reject is selected
        document.querySelectorAll('input[name="package_decision"]').forEach(radio => {
            radio.addEventListener('change', function() {
                const reasonSelect = document.querySelector('.dp-sub-reasons');
                if (this.value === 'reject') {
                    reasonSelect.style.display = 'block';
                } else {
                    reasonSelect.style.display = 'none';
                }
            });
        });"""

content = content.replace(js_search, "")

with open('packages.html', 'w') as f:
    f.write(content)
