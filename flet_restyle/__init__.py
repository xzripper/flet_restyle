"""Flet ReStyle."""

# from flet import Page, Theme, ThemeVisualDensity, WindowDragArea, AppBar, IconButton, Icon, Text, colors, icons

from flet import Page, Theme, ThemeVisualDensity, WindowDragArea, Container, Row, IconButton, Icon, Text, colors, icons

from BlurWindow.blurWindow import GlobalBlur

from ctypes import windll

from typing import Callable


def google_font(font_folder: str, font: str) -> tuple[str, str]:
    """Returns font name, and link on a google font."""
    return (font, f'https://github.com/google/fonts/raw/main/apache/{font_folder}/{font}.ttf')

class FletReStyleConfig:
    """ReStyle Config."""
    theme: Theme = Theme(colors.PURPLE_ACCENT_700, visual_density=ThemeVisualDensity.ADAPTIVEPLATFORMDENSITY, font_family='RobotoMono[wght]')

    font: tuple[str, str] = google_font('robotomono', 'RobotoMono[wght]')

    dark: bool = True

    background: str = colors.with_opacity(0.1, colors.WHITE)

    frameless: bool = True

    custom_title_bar: bool = True

    custom_title_bar_icon: str = icons.APPS

    custom_title_bar_title: str = 'Application'

    custom_title_bar_allowed_to_maximize: bool = True

    transparent_background: bool = True

class FletReStyle:
    @staticmethod
    def apply_config(page: Page, config: FletReStyleConfig, _page_on_resize_event: Callable=None) -> None:
        if config.font:
            if page.fonts:
                page.fonts[config.font[0]] = config.font[1]

            else:
                page.fonts = {config.font[0]: config.font[1]}

        page.theme = config.theme

        page.theme_mode = 'dark' if config.dark else 'light'

        page.bgcolor = config.background

        if config.frameless:
            page.window_title_bar_hidden = True

            page.window_frameless = True

        if config.custom_title_bar:
            # https://github.com/flet-dev/flet/issues/2051
            # title_bar = AppBar(
            #     leading=Icon(config.custom_title_bar_icon),
            #     leading_width=50,

            #     title=Text(config.custom_title_bar_title),
            #     center_title=True,

            #     bgcolor=colors.SURFACE_VARIANT,

            #     actions=[
            #         IconButton(icons.CIRCLE_OUTLINED, on_click=lambda _: [setattr(page, 'window_minimized', not page.window_minimized), page.update()], icon_color=colors.AMBER, icon_size=25),
            #         IconButton(icons.CROP_SQUARE, on_click=lambda _: [setattr(page, 'window_maximized', not page.window_maximized), page.update()], icon_color=colors.GREEN, icon_size=25),
            #         IconButton(icons.CLOSE_ROUNDED, on_click=lambda _: page.window_close(), icon_color=colors.RED, icon_size=25)
            #     ]
            # )

            title_bar = Container(
                Row([
                    Container(
                        Row([
                            Icon(config.custom_title_bar_icon, size=30)
                        ])
                    ),

                    Container(
                        Row([
                            Text(config.custom_title_bar_title, size=25)
                        ])
                    ),

                    Container(
                        Row([
                            IconButton(
                                icons.CIRCLE_OUTLINED,

                                on_click=lambda _: [
                                    setattr(page, 'window_minimized', not page.window_minimized), page.update()
                                ],

                                icon_color=colors.AMBER, icon_size=30
                            ),

                            IconButton(
                                icons.CROP_SQUARE,

                                on_click=lambda _: [
                                    setattr(page, 'window_maximized', not page.window_maximized) if config.custom_title_bar_allowed_to_maximize else None, page.update()
                                ], 

                                icon_color=colors.GREEN if config.custom_title_bar_allowed_to_maximize else colors.GREY,

                                icon_size=30,

                                disabled=not config.custom_title_bar_allowed_to_maximize
                            ),

                            IconButton(
                                icons.CLOSE_ROUNDED,

                                on_click=lambda _: page.window_close(),

                                icon_color=colors.RED, icon_size=30
                            )
                        ])
                    )
                ], alignment='spaceBetween'), bgcolor=colors.SURFACE_VARIANT, padding=10
            )

            page.on_resize = lambda _: [_page_on_resize_event() if _page_on_resize_event else None, setattr(title_bar, 'width', page.window_width)]

            page.add(WindowDragArea(title_bar))

        if config.transparent_background:
            HWND = windll.user32.GetForegroundWindow()

            if HWND:
                GlobalBlur(HWND, Dark=True)

        page.update()
