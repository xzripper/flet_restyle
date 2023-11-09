<h1 align="center">Flet ReStyle Documentation v1.0.0.</h1>
<h3 align="center"><code>FletReStyleConfig</code></h3>

```python
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
```
Used to create config and then apply to your page.<br>
`frameless`, `custom_title_bar`, `custom_title_bar_icon`, `custom_title_bar_allowed_to_maximize`, `transparent_background` - Supported only in Desktop version.<br>

<h3 align="center"><code>FletReStyle</code></h3>

```python
class FletReStyle:
    @staticmethod
    def apply_config(page: Page, config: FletReStyleConfig, _page_on_resize_event: Callable=None) -> None
```
`apply_config` used to apply your config to page. `_page_on_resize_event` will be called on_resize.

<h3 align="center"><code>google_font</code></h3>

```python
google_font(font_folder: str, font: str) -> tuple[str, str] # google_font('robotomono', 'RobotoMono[wght]') => https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono[wght].ttf
```
Used to get google font easily.
