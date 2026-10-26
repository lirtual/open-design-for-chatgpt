# UI state coverage

For a data-backed view, make the **loading**, **empty**, **error**, **populated** and **edge** states visible and understandable. If data is simulated, label it explicitly. Preserve form input on validation errors and provide recovery actions. For interactive forms, account for untouched, valid/dirty, invalid and submitting states. Each state needs sensible keyboard focus and non-color-only status cues. Verify using runnable fixtures when possible; do not claim a five-state runtime implementation when only the populated view was built.
