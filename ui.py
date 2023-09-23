import matplotlib
import matplotlib.pyplot as plt
import flet as ft
from ozon_calculator import OzonCalculator
from flet.matplotlib_chart import MatplotlibChart


matplotlib.use("svg")
output = None
calculated = None


def main(page: ft.Page):
    page.window_height = 475
    page.window_width = 500
    page.window_resizable = False
    page.title = "Ozon Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def calculate(e):
        global output, calculated

        calc = OzonCalculator(filament_weight=int(filament_weight_input.value),
                              filament_price=int(filament_price_input.value),
                              package_price=int(package_price_input.value),
                              marketing_price=int(marketing_price_input.value) / 100,
                              ozon_cut=int(ozon_cut_input.value) / 100)

        calculated = calc.calculate_profit(selling_price=int(selling_price_input.value))
        if int(calculated) > 0:

            labels = "Стоимость \nупаковки", "Доля Озона", "Рекламные расходы \n(Озон)", \
                "Стоимость пластика", "Чистая прибыль"

            fragments = [
                package_price_input.value,
                float(selling_price_input.value) * (float(ozon_cut_input.value) / 100),
                float(selling_price_input.value) * (float(marketing_price_input.value) / 100),
                (float(filament_price_input.value) / 1000) * float(filament_weight_input.value),
                float(calculated)
            ]
            fig, ax = plt.subplots()
            ax.pie(fragments,
                   labels=labels,
                   autopct='%1.0f%%',
                   explode=(0.02, 0.02, 0.02, 0.02, 0.15),
                   colors=["#729ea1", "#dfbe99", "#ec9192", "#db5375", "#b5bd89"],
                   )

            output = ft.Column(
                [
                    ft.Text("Чистая прибыль:", size=40, weight="bold", color="#b5bd89"),
                    ft.Text(str(calculated.__format__('.2f') + "₽"), size=75, weight="bold", color="#b5bd89"),
                    ft.Divider(
                        height=20
                    ),
                    MatplotlibChart(fig)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        else:
            output = ft.Column(
                [
                    ft.Text("Чистая прибыль:", size=40, weight="bold", color="#db5375"),
                    ft.Text(str(calculated.__format__('.2f') + "₽"), size=75, weight="bold", color="#db5375"),
                    ft.Divider(
                        height=20
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        return calculated, output

    def clear_value(e):
        selling_price_input.value = ""
        selling_price_input.update()

    def redraw_content(e):
        calculate(e="")
        page.clean()

        if int(calculated) > 0:
            page.window_height = 1000
        else:
            page.window_height = 685

        page.add(
            ft.Column(
                [
                    ft.Divider(
                        height=20
                    ),
                    ft.Row(
                        [
                            filament_price_input,
                            filament_weight_input,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        width=page.window_width,
                    ),
                    ft.Row(
                        [
                            package_price_input,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        width=page.window_width,
                    ),
                    ft.Row(
                        [
                            ozon_cut_input,
                            marketing_price_input,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        width=page.window_width,
                    ),
                    ft.Divider(
                        height=20,
                    )
                ]
            ),
            ft.Column(
                [
                    selling_price_input,
                    ft.Divider(
                        height=20,
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                width=page.window_width,
            ),
            output,
            # ft.Divider(
            #   height=20,
            # ),
            button,
        )

        page.update()

    def draw_pie_chart(e):

        labels = "Стоимость упаковки", "Доля Озона", "Рекламные расходы (Озон)", "Стоимость пластика", "Чистая прибыль"

        fragments = [
            package_price_input.value,
            float(selling_price_input.value) * (float(ozon_cut_input.value) / 100),
            float(selling_price_input.value) * (float(marketing_price_input.value) / 100),
            (float(filament_price_input.value) / 1000) * float(filament_weight_input.value),
            float(calculated)
        ]
        fig, ax = plt.subplots()
        ax.pie(fragments,
               labels=labels,
               autopct='%1.0f%%',
               explode=(0.02, 0.02, 0.02, 0.02, 0.1),
               colors=["#729ea1", "#dfbe99", "#ec9192", "#db5375", "#b5bd89"]
               )

    selling_price_input = ft.TextField(label="Цена продажи", suffix_text="₽", width=422, value="550",
                                       on_submit=redraw_content, on_focus=clear_value)
    profit_input = ft.TextField(label="Прибыль с продажи", suffix_text="₽", width=422)
    filament_price_input = ft.TextField(label="Стоимость филамента", suffix_text="₽", value="1500", width=200)
    filament_weight_input = ft.TextField(label="Расход филамента", suffix_text="гр", value="45",width=200)
    package_price_input = ft.TextField(label="Стоимость упаковки", suffix_text="₽", value="30", width=422)
    ozon_cut_input = ft.TextField(label="Доля Озона", suffix_text="%",value="35", width=200)
    marketing_price_input = ft.TextField(label="Рекламные расходы (Озон)", suffix_text="%", value="20", width=200)
    button = ft.FloatingActionButton(icon=ft.icons.CALCULATE_OUTLINED, on_click=redraw_content)
    chart_button = ft.IconButton(icon=ft.icons.PIE_CHART, on_click=draw_pie_chart)

    page.add(
        ft.Column(
            [
                ft.Divider(
                    height=20
                ),
                ft.Row(
                    [
                        filament_price_input,
                        filament_weight_input,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    width=page.window_width,
                ),
                ft.Row(
                    [
                        package_price_input,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    width=page.window_width,
                ),
                ft.Row(
                    [
                        ozon_cut_input,
                        marketing_price_input,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    width=page.window_width,
                ),
                ft.Divider(
                    height=20,
                )
            ]
        ),
        ft.Column(
            [
                selling_price_input,
                ft.Divider(
                    height=20,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=page.window_width,
        ),
        button,
    )

    page.update()


ft.app(target=main)
