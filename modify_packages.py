import re

def main():
    with open('packages.html', 'r') as f:
        content = f.read()

    # Replace titles
    content = content.replace('Chat Moderation Queue', 'Package Moderation Queue')
    content = content.replace('Evaluate reported chat threads between suppliers and clients for safety and policy violations.', 'Evaluate new items or services being sold by suppliers.')
    content = content.replace('<title>Lumera Admin - Chat Moderation</title>', '<title>Lumera Admin - Package Moderation</title>')

    # Update sidebar active state
    content = content.replace('<a href="chat.html" class="nav-item active">', '<a href="chat.html" class="nav-item">')
    content = content.replace('<a href="packages.html" class="nav-item">', '<a href="packages.html" class="nav-item active">')

    # Update list headers
    content = content.replace('<th>REPORTED PARTY</th>', '<th>PACKAGE TITLE</th>')
    content = content.replace('<th>REPORTED BY</th>', '<th>SUPPLIER</th>')
    content = content.replace('<th>FLAG REASON</th>', '<th>CATEGORY</th>')
    content = content.replace('<th>DATE FLAGGED</th>', '<th>PRICE</th>')

    # Update list rows (we'll just replace the entire tbody contents for simplicity)
    list_tbody = """
                    <tbody>
                        <tr>
                            <td>
                                <div class="biz-name">Intimate Garden Setup</div>
                                <div class="biz-category">Lumera Events Co.</div>
                            </td>
                            <td>Anna Reyes</td>
                            <td class="cell-email">Event Styling</td>
                            <td class="cell-date">₱15,000.00</td>
                            <td><span class="status-badge" style="background-color: #fef08a; color: #854d0e; border: 1px solid #fde047;">Pending Review</span></td>
                            <td><button class="btn-submit" style="padding: 6px 16px; font-size: 13px;" onclick="showDetail()">Moderate</button></td>
                        </tr>
                    </tbody>
    """

    # Find and replace tbody content in list container
    tbody_start = content.find('<tbody>')
    tbody_end = content.find('</tbody>', tbody_start) + len('</tbody>')

    content = content[:tbody_start] + list_tbody.strip() + content[tbody_end:]


    # Now replace the view-detail block
    view_detail_html = """
            <!-- ACTIVE MODERATION DETAIL VIEW (PENDING TASK) -->
            <div id="view-detail" style="display: none;">
                <div class="page-header" style="display: block;">
                    <h1>Moderate Package: Intimate Garden Setup</h1>
                    <p>Review the package details and media provided by the supplier.</p>
                </div>

                <div class="verification-blocks">
                    <div class="mod-block">

                        <!-- Col 1: Package Details -->
                        <div class="block-data">
                            <div class="block-header">
                                <i class="ph-fill ph-package"></i> 1. Package Details
                            </div>

                            <div class="info-grid">
                                <div class="info-item">
                                    <div class="label">Package Title</div>
                                    <div class="value">Intimate Garden Setup</div>
                                </div>
                                <div class="info-item">
                                    <div class="label">Supplier</div>
                                    <div class="value">Lumera Events Co.</div>
                                </div>
                                <div class="info-item">
                                    <div class="label">Category</div>
                                    <div class="value">Event Styling</div>
                                </div>
                                <div class="info-item">
                                    <div class="label">Price</div>
                                    <div class="value">₱15,000.00</div>
                                </div>
                                <div class="info-item">
                                    <div class="label">Description</div>
                                    <div class="value" style="font-style: italic; font-size: 13px;">
                                        "A beautiful setup for intimate garden events."
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Col 2: Media Viewer -->
                        <div class="block-action">
                            <div class="doc-preview-label">Package Media</div>
                            <div class="evidence-gallery" style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                                <div class="evidence-thumb" style="height: 150px; overflow: hidden; border-radius: 6px; border: 1px solid var(--border-color);">
                                    <img src="https://images.unsplash.com/photo-1544597441-2a6286ebfb93?w=400&q=80" class="clickable-img" onclick="openMediaModal(this)" style="width: 100%; height: 100%; object-fit: cover; cursor: zoom-in; transition: transform 0.2s;">
                                </div>
                                <div class="evidence-thumb" style="height: 150px; overflow: hidden; border-radius: 6px; border: 1px solid var(--border-color);">
                                    <img src="https://images.unsplash.com/photo-1519225421980-715cb0215aed?w=400&q=80" class="clickable-img" onclick="openMediaModal(this)" style="width: 100%; height: 100%; object-fit: cover; cursor: zoom-in; transition: transform 0.2s;">
                                </div>
                            </div>
                        </div>

                        <!-- Col 3: Decision Panel -->
                        <div class="block-decision">
                            <div class="dp-title"><i class="ph-fill ph-gavel"></i> Moderator Decision</div>
                            <div class="decision-wrapper">
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
                            </div>
                        </div>
                    </div>

                    <!-- Final Action Bar -->
                    <div class="final-action-bar">
                        <div class="final-action-text">
                            <h4>Submit Moderation Decision</h4>
                            <p>Once submitted, the package will be updated accordingly.</p>
                        </div>
                        <button class="btn-submit" onclick="submitDecision()">Submit Decision</button>
                    </div>
                </div>
            </div>
    """

    # We will replace all the views with our new view-detail block
    view_start = content.find('<div id="view-detail"')
    if view_start == -1:
        # Fallback if structure is different
        view_start = content.find('<!-- ACTIVE MODERATION DETAIL VIEW')

    main_end = content.find('</main>')

    # Just replace everything from view-detail to the end of main
    content = content[:view_start] + view_detail_html.strip() + "\n\n        " + content[main_end:]

    # Add JS functionality at the bottom for openMediaModal and navigation if missing
    if 'function openMediaModal' not in content:
        js_code = """
    <!-- --- MEDIA VIEWER MODAL --- -->
    <div class="media-modal-overlay" id="media-modal" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(17, 24, 39, 0.9); z-index: 9999; display: none; flex-direction: column; align-items: center; justify-content: center; backdrop-filter: blur(4px);">
        <div class="media-modal-controls" style="position: absolute; top: 20px; right: 20px; display: flex; gap: 12px;">
            <button onclick="closeMediaModal()" style="background: rgba(255,255,255,0.1); color: white; border: none; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; font-size: 20px;"><i class="ph ph-x"></i></button>
        </div>
        <div class="media-modal-content" style="position: relative; max-width: 90vw; max-height: 85vh; display: flex; align-items: center; justify-content: center;">
            <img id="modal-img-target" src="" alt="Expanded Media" style="max-width: 100%; max-height: 75vh; object-fit: contain; transition: transform 0.2s ease-out; box-shadow: 0 10px 25px rgba(0,0,0,0.5); border-radius: 4px;">
        </div>
    </div>

    <script>
        // List/Detail Toggle
        const viewList = document.getElementById('view-list');
        const viewDetail = document.getElementById('view-detail');

        function showDetail() {
            viewList.style.display = 'none';
            viewDetail.style.display = 'block';
            window.scrollTo(0,0);
        }

        function showList() {
            viewDetail.style.display = 'none';
            viewList.style.display = 'block';
            window.scrollTo(0,0);
        }

        function submitDecision() {
            alert('Decision submitted!');
            showList();
        }

        // --- MEDIA VIEWER ---
        const modalEl = document.getElementById('media-modal');
        const modalImgTarget = document.getElementById('modal-img-target');

        function openMediaModal(clickedImg) {
            modalImgTarget.src = clickedImg.src;
            modalEl.style.display = 'flex';
        }

        function closeMediaModal() {
            modalEl.style.display = 'none';
        }

        // Show reason dropdown when Reject is selected
        document.querySelectorAll('input[name="package_decision"]').forEach(radio => {
            radio.addEventListener('change', function() {
                const reasonSelect = document.querySelector('.dp-sub-reasons');
                if (this.value === 'reject') {
                    reasonSelect.style.display = 'block';
                } else {
                    reasonSelect.style.display = 'none';
                }
            });
        });
    </script>
</body>
</html>"""
        # Replace the closing tags with our JS injected
        content = content.replace('</body>\n</html>', js_code)

    with open('packages.html', 'w') as f:
        f.write(content)

if __name__ == "__main__":
    main()
