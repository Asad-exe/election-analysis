
        ax.set_ylabel("Winning Margin")

    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    plt.close(fig)

update_btn = tk.Button(control_frame, text="Update Chart", command=draw_chart, bg="#4CAF50", fg="white")
update_btn.grid(row=0, column=4, padx=10)

# Draw initial chart
draw_chart()

root.mainloop()