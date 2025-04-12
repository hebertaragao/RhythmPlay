import flet as ft
def main(page: ft.Page):

    page.title = "Analisador de Ritmo"
    page.theme_mode = ft.ThemeMode.LIGHT 

    # Elementos da Interface

    ritmo_text = ft.Text("Ritmo: Nenhum arquivo carregado")
    bpm_text = ft.Text("BPM: ---")
    volume_text = ft.Text("Volume: 50%")

    bpm_slider = ft.Slider(min=40, max=200, value=120, label="BPM", divisions=160)
    volume_slider = ft.Slider(min=0, max=100, value=50, label="Volume", divisions=100)

    theme_toggle = ft.Switch(label="Modo Escuro")

    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if theme_toggle.value else ft.ThemeMode.LIGHT
        page.update()   

    theme_toggle.on_change = toggle_theme

    # Upload de áudio
    upload = ft.FilePicker()
    page.overlay.append(upload)

    def on_file_upload(e):
        file_path = upload.result.files[0].path
        ritmo_text.value = f"Analisando: {file_path.split('/')[-1]}"
        page.update()

        # Aqui você chamaria a função de detecção de ritmo
        ritmo, bpm_detectado = detectar_ritmo(file_path)
        ritmo_text_value = f"Ritmo: {ritmo}"
        bpm_text_value = f"BPM: {bpm_detectado}"
        page.update()

    upload.on_result = on_file_upload
    carregar_btn = ft.ElevatedButton("Carregar Áudio", on_click=lambda _: upload.pick_files())


    # Layout final

    page.add(
        ft.Column([
            ritmo_text,
            bpm_text,
            volume_text,
            bpm_slider,
            volume_slider,
            carregar_btn,
            theme_toggle
        ])
    )

ft.app(target=main)


