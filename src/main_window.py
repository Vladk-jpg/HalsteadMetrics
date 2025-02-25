import tkinter as tk
from tkinter import ttk
from compute_metrics import compute_metrics

def show_table(operators: dict, operands: dict):
    metrics = compute_metrics(operators, operands)

    root = tk.Tk()
    root.title("Таблица операторов и операндов")
    root.geometry("800x600")

    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure("Custom.Treeview",
                    font=("Segoe UI", 12),
                    borderwidth=2,
                    relief="solid",
                    rowheight=25,
                    background="white",
                    fieldbackground="white")

    style.configure("Custom.Treeview.Heading",
                    font=("Segoe UI", 12, "bold"),
                    borderwidth=2,
                    relief="solid",
                    background="#d9d9d9")

    style.layout("Custom.Treeview.Heading", [
        ("Custom.Treeview.Heading.cell", {"sticky": "nswe"}),
        ("Custom.Treeview.Heading.border", {"sticky": "nswe", "children": [
            ("Custom.Treeview.Heading.padding", {"sticky": "nswe", "children": [
                ("Custom.Treeview.Heading.image", {"side": "right", "sticky": ""}),
                ("Custom.Treeview.Heading.text", {"sticky": "we"})
            ]})
        ]})
    ])
    style.configure("Custom.Treeview.Heading.cell", borderwidth=1, relief="solid")
    style.configure("Custom.Treeview.Heading.border", borderwidth=1, relief="solid")

    frame_table = ttk.Frame(root)
    frame_table.pack(expand=True, fill="both")

    vsb = ttk.Scrollbar(frame_table, orient="vertical")
    hsb = ttk.Scrollbar(frame_table, orient="horizontal")

    columns = ("j", "Оператор", "f1j", "i", "Операнд", "f2i")
    tree = ttk.Treeview(
        frame_table,
        columns=columns,
        show="headings",
        style="Custom.Treeview",  
        yscrollcommand=vsb.set,
        xscrollcommand=hsb.set
    )

    vsb.config(command=tree.yview)
    hsb.config(command=tree.xview)

    vsb.pack(side=tk.RIGHT, fill=tk.Y)
    hsb.pack(side=tk.BOTTOM, fill=tk.X)
    tree.pack(expand=True, fill="both")

    tree.column("j", width=40, anchor=tk.CENTER)
    tree.column("Оператор", width=180, anchor=tk.W)
    tree.column("f1j", width=60, anchor=tk.CENTER)
    tree.column("i", width=40, anchor=tk.CENTER)
    tree.column("Операнд", width=180, anchor=tk.W)
    tree.column("f2i", width=60, anchor=tk.CENTER)

    tree.heading("j", text="j")
    tree.heading("Оператор", text="Оператор")
    tree.heading("f1j", text="f1j")
    tree.heading("i", text="i")
    tree.heading("Операнд", text="Операнд")
    tree.heading("f2i", text="f2i")

    tree.tag_configure("oddrow", background="#ffffff")
    tree.tag_configure("evenrow", background="#f0f0f0")

    op_keys = list(operators.keys())
    op_vals = list(operators.values())
    operand_keys = list(operands.keys())
    operand_vals = list(operands.values())

    max_rows = max(len(operators), len(operands))
    for i in range(max_rows):
        operator_key = op_keys[i] if i < len(op_keys) else ""
        operator_val = op_vals[i] if i < len(op_vals) else ""
        operand_key = operand_keys[i] if i < len(operand_keys) else ""
        operand_val = operand_vals[i] if i < len(operand_vals) else ""

        row_tag = "oddrow" if i % 2 == 0 else "evenrow"
        tree.insert(
            "",
            tk.END,
            values=(
                i + 1,
                operator_key,
                operator_val,
                i + 1,
                operand_key,
                operand_val
            ),
            tags=(row_tag,)
        )

    tree.insert(
        "",
        tk.END,
        values=(
            "",
            f"n1 = {metrics['n1']}",
            f"N1 = {metrics['N1']}",
            "",
            f"n2 = {metrics['n2']}",
            f"N2 = {metrics['N2']}"
        ),
        tags=("oddrow",)  
    )

    tree.insert("", tk.END, values=("", "", "", "", "", ""), tags=("evenrow",))

    tree.insert("", tk.END, values=("", f"n = {metrics['n']}", "", "", "", ""), tags=("oddrow",))
    tree.insert("", tk.END, values=("", f"N = {metrics['N']}", "", "", "", ""), tags=("evenrow",))
    tree.insert("", tk.END, values=("", f"Volume = {metrics['Volume']:.2f}", "", "", "", ""), tags=("oddrow",))

    root.mainloop()
