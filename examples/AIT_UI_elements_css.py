""" 
    
	<div class="header">
	    <img class="logo" src="AIT_AI_LOGO.png">
	</div>
	
	<h1>Örnek Girdi Alanları</h1>

    <label for="text-input">Metin Girdi Alanı:</label>
    <input type="text" id="text-input" name="text_input" value="Umut Savaşım"><br><br>

    <label for="password-input">Parola Girdi Alanı:</label>
    <input type="password" id="password-input" name="password_input" value="ASdadgsdfgASD@"><br><br>

    <label for="email-input">E-posta Girdi Alanı:</label>
    <input type="email" id="email-input" name="email_input" value="umut@ait.com.tr"><br><br>

    <label for="number-input">Sayı Girdi Alanı:</label>
    <input type="number" id="number-input" name="number_input" value="15"><br><br>
	
	<label for="bos_input">Boş test:</label>
    <input type="text" id="number-input" name="bos_input" value="" placeholder="Yazınız.."><br><br>

    <label for="date-input">Tarih Girdi Alanı:</label>
    <input type="date" id="date-input" name="date_input"><br><br>

<div class="row">
    <label for="checkbox-input">Onay Kutusu:</label>
    <input type="checkbox" id="checkbox-input" name="checkbox_input"><br><br>
</div>
<div class="row">
    <label for="checkbox-input1">Onay Kutusu:</label>
    <input type="checkbox" id="checkbox-input1" name="checkbox_input"><br><br>
</div>
<div class="row">
    <label for="checkbox-input2">Onay Kutusu:</label>
    <input type="checkbox" id="checkbox-input2" name="checkbox_input"><br><br>
</div>

<div class="col" style="gap:10px;">
	<div class="row">
		<label for="radio-input-1">Radyo Düğmesi 1:</label>
		<input type="radio" id="radio-input-1" name="radio_input" value="option1"><br>
	</div>
	<div class="row">
		<label for="radio-input-2">Radyo Düğmesi 2:</label>
		<input type="radio" id="radio-input-2" name="radio_input" value="option2"><br>
	</div>
		<div class="row">
		<label for="radio-input-3">Radyo Düğmesi 3:</label>
		<input type="radio" id="radio-input-3" name="radio_input" value="option1"><br>
	</div>
	<div class="row">
		<label for="radio-input-4">Radyo Düğmesi 4:</label>
		<input type="radio" id="radio-input-4" name="radio_input" value="option2"><br>
	</div>
</div>

    <label for="textarea-input">Metin Alanı:</label><br>
    <textarea id="textarea-input" name="textarea_input" style="width: 250px;">Umut Savaşım Çeliker Umut Savaşım Çeliker Umut Savaşım Çeliker Umut Savaşım Çeliker </textarea><br><br>

    <label for="select-input">Açılır Liste:</label>
    <select id="select-input" name="select_input">
        <option value="option1">Seçenek 1</option>
        <option value="option2">Seçenek 2</option>
        <option value="option3">Seçenek 3</option>
		<option value="option1">Seçenek 1</option>
        <option value="option2">Seçenek 2</option>
        <option value="option3">Seçenek 3</option>
		<option value="option1">Seçenek 1</option>
        <option value="option2">Seçenek 2</option>
        <option value="option3">Seçenek 3</option>
		<option value="option1">Seçenek 1</option>
        <option value="option2">Seçenek 2</option>
        <option value="option3">Seçenek 3</option>
		<option value="option1">Seçenek 1</option>
        <option value="option2">Seçenek 2</option>
        <option value="option3">Seçenek 3</option>
		<option value="option1">Seçenek 1</option>
        <option value="option2">Seçenek 2</option>
        <option value="option3">Seçenek 3</option>
    </select><br><br>

    <label for="file-input">Dosya Yükleme Alanı:</label>
    <input type="file" id="file-input" name="file_input"><br><br>

    <label for="color-input">Renk Seçim Alanı:</label>
    <input type="color" id="color-input" name="color_input"><br><br>
	
	<label for="slider">Standart Slider:</label>
	<input type="range" id="color-input" name="slider" min="1" max="100" value="25"><br><br>
	
	<div class="row" style="gap:10px;">
	<button>Umut Savaşım Çeliker</button> <button class="btn-reset">Resetle</button> <button class="btn-warning">Uyarı</button> <button class="btn-red">Silinecek</button>
	</div>"""

#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
ait_comp_path = "D:\\Work\\Dev\\Projects\\ait-ui-examples\\components"
sys.path.append(ait_comp_path)
from comp_alert import Comp_Alert
# ----------------------------------------
from ait_ui import app
from ait_ui.elements import ImageViewer, Row, Slider, Radio, Label, Image, Header, Text, Htext, Input, TextArea, Select, Option, Button, Col, Check
from ait_ui.core import Component, Elm, Element

class CSS_TEST(Component):
    def __init__(self, id=None, autoBind=True, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)
        with self:
            # if need notifications add this class
            self.alert = Comp_Alert(id="globalAlert")
            with Header():
                Image(value="AIT_AI_LOGO.png").cls("logo")
            
            Htext(tag="1", value="Örnek Girdi Alanları")
            with Row().style("gap","10px"):   
                with Col().style("align-items","flex-start").style("width","fit-content").style("gap","10px"):
                    Label(usefor="text-input", value="Metin Girdi Alanı:")
                    Input(type="text", id="text-input", value="Umut Savaşım")

                    Label(usefor="password-input", value="Parola Girdi Alanı:")
                    Input(type="password", id="password-input", value="ASdadgsdfgASD@")

                    Label(usefor="email-input", value="E-posta Girdi Alanı:")
                    Input(type="email", id="email-input", value="umut@ait.com.tr")

                    Label(usefor="number-input", value="Sayı Girdi Alanı:")
                    Input(type="number", id="number-input", value="15")

                    Label(usefor="bos-input", value="Boş test:")
                    Input(type="text", id="bos-input", value="", placeholder="Yazınız..")

                    Label(usefor="disable-input", value="Disable Test (CSS Test):").cls("disabled")
                    Input(type="text", id="disable-input", value="", placeholder="Bu alan erişilemez..").disabled()

                    Label(usefor="date-input", value="Tarih Girdi Alanı:")
                    Input(type="date", id="date-input")

                    Label(usefor="textarea-input", value="Disable Metin Alanı:")
                    TextArea(id="textarea-input", value="Umut Savaşım Çeliker Umut Savaşım Çeliker Umut Savaşım Çeliker Umut Savaşım Çeliker").style("width","250px").disabled()

                with Col().style("width","fit-content").style("gap","10px"):
                    with Row().style("justify-content","flex-start"):
                        Label(usefor="checkbox-input", value="Onay Kutusu:")
                        Input(type="checkbox", id="checkbox-input")

                    with Row().style("justify-content","flex-start"):
                        Label(usefor="checkbox-input2", value="Pasif Kutu:")
                        Input(type="checkbox", id="checkbox-input2").disabled()

                    with Col().style("align-items","flex-start"):
                        with Row().style("justify-content","flex-start"):
                            Label(usefor="radio-input-1", value="Radyo Düğmesi 1:")
                            Radio(name="radyolar", id="radio-input-1", value="option1")

                        with Row().style("justify-content","flex-start"):
                            Label(usefor="radio-input-2", value="Radyo Düğmesi 2:")
                            Radio(name="radyolar", id="radio-input-2", value="option2")

                        with Row().style("justify-content","flex-start"):
                            Label(usefor="radio-input-3", value="Seçili Ama Seçilemez:")
                            Radio(name="radyolar", id="radio-input-3", value="option3").checked().disabled()

                        with Row().style("justify-content","flex-start"):
                            Label(usefor="radio-input-4", value="Radyo Düğmesi 4:")
                            Radio(name="radyolar", id="radio-input-4", value="option4")

                        with Row().style("justify-content","flex-start"):
                            Label(usefor="radio-input-5", value="Radyo Düğmesi 5:")
                            Radio(name="radyolar", id="radio-input-5", value="option5")

                    Label(usefor="textarea-input", value="Metin Alanı:")
                    TextArea(id="textarea-input", value="Umut Savaşım Çeliker Umut Savaşım Çeliker Umut Savaşım Çeliker Umut Savaşım Çeliker").style("width","250px")

                    Label(usefor="select-input", value="Açılır Liste:")
                    with Select(id="select-input").style("width","250px"):
                        Option(value="option1", text="Seçenek 1")
                        Option(value="option2", text="Seçilemeyen").disabled()
                        Option(value="option3", text="Seçili Gelen").selected()

                    Label(usefor="file-input", value="Dosya Yükleme Alanı:")
                    Input(type="file", id="file-input").style("width","250px")

                    Label(usefor="color-input", value="Renk Seçim Alanı:")
                    Input(type="color", id="color-input")

                    Label(usefor="slider", value="Standart Slider:")
                    Slider(id="slider", min="1", max="100", value="25")

                    Label(usefor="slider", value="Disabled Slider:")
                    Slider(id="slider", min="1", max="100", value="25").disabled()

                    with Row().style("gap","10px;").style("justify-content","flex-start"):
                        Button(value="Umut Savaşım Çeliker").on("click", lambda id, value: self.alert.open("alert-success","Onay mesajı"))
                        Button(value="Resetle").on("click", lambda id, value: self.alert.open("alert-normal","Normal mesaj")).cls("btn-reset")
                        Button(value="Uyarı").on("click", lambda id, value: self.alert.open("alert-warning","Uyarı mesajı")).cls("btn-warning")
                        Button(value="Silinecek").on("click", lambda id, value: self.alert.open("alert-danger","Tehlikeli mesaj")).cls("btn-red")
                        Button(value="Disable", disabled=True)
                        Button(value="Bilgi").on("click", lambda id, value: self.alert.open("alert-info","Bilgilendirme mesajı")).cls("btn-info")

if __name__ == '__main__':
    app.run(ui=CSS_TEST, debug=True)
