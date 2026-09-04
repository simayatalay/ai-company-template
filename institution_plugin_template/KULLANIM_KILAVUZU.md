# Institution Plugin Template – Türkçe Kullanım Kılavuzu
## 1. Bu Template Nedir?
Institution Plugin Template,QGIS için yeni bir plugin geliştirirken başlangıç noktası olarak kullanılabilecek örnek bir plugin şablonudur.

Bu projenin amacı,QGIS plugin geliştirmeyi hiç bilmeyen bir geliştiricisinin bile projeyi açtıktan sonra:

-dosya yapısını anlayabilmesi,
-hangi dosyanın ne işe yaradığını öğrenebilmesi,
-hazır widget örneklerini inceleyebilmesi,
-ihtiyacı olan widget örneklerini kendi plugininde kullanabilmesi,
-yeni widget ekleyebilmesi,
-widget'lara python davranışı ekleyebilmesi,
-plugin bilgilerini değiştirebilmesi,
-plugin'i QGIS içerisinde çalıştırıp test edebilmesi

için hazır bir başlangıç ortamı sağlmaktır.

Bu template yalnızca çalışan bir template değildir.Aynı zamanda QGIS plugin geliştirme sürecini öğretmek amacıyla hazırlanmış örnekler içerir.

---

# 2. Template'i İlk Açtığımda Ne Göreceğim?

Projeyi ilk açtığınızca QGIS pluginin temel dosyaları ile karşılaşırsınız.

Önemli dosyalar:

```text
institution_plugin_template/
│
├── __init__.py
├── metadata.txt
├── icon.png
├── institution_plugin_template.py
├── institution_plugin_template_dialog.py
├── institution_plugin_template_dialog_base.ui
├── KULLANIM_KILAVUZU.md
│
└── widgets/
    ├── __init__.py
    ├── README.md
    └── widget_examples.py
    ```

---
# 3. Hangi Dosya Ne İşe Yarar?

Bu bölümde template içerisinde bulunan temel dosyaların görevleri açıklanmaktadır.

## `__init__.py`

QGIS'in bu klasörü bir Python paketi ve plugin olarak tanıyabilmesi için kullanılan başlangıç dosyalarından biridir.

Genellikle plugin yüklenirken ana plugin sınıfının QGIS tarafından oluşturulmasını sağlar.

Yeni başlayan kişi çoğu durumda bu dosyada değişiklik yapmak zorunda değildir.

---

## `metadata.txt`

Plugin hakkında QGIS'e bilgi veren dosyadır.

Bu dosyada örneğin:

-plugin adı,
-açıklaması,
-sürüm numarası,
-yazar bilgisi,
-kategori,
-plugin hakkında diğer bilgiler

bulunabilir.

### Ne zaman bu dosyayı değiştirmeliyim?

Örneğin template'i kullanarak kendi plugininizi oluşturduğunuzda plugin adını ve sürümünü değiştirmek için bu dosyayı düzenleyebilirsiniz.

---


## `icon.png`

Plugin'in QGIS içerisinde kullanacağı ikon dosyasıdır.

Kendi plugininizi geliştirirken örnek ikonu kendi plugin ikonunuzla değiştirebilirsiniz.

---

## 
`institution_plugin_template.py`

Plugin'in QGIS ile bağlantısını yöneten ana python dosyalarından biridir.

Bu dosya:

-plugin'in QGIS'e eklenmesi,
-menü işlemleri,
-toolbar işlemleri
-plugin penceresinin eklenmesi

gibi işlemlerde kullanılır.

### Ne zaman bu dosyaya bakmalıyım?

Plugin'in QGIS içerisindeki genel davranışını değiştirmek istediğinizde bu dosyaya bakabilirsiniz.

---

## `institution_plugin_template_dialog_base.ui`

Plugin'in kullanıcı arayüzlerini tanımlayan dosyadır.

Ekranda gördüğünüz:

-butonlar,
-yazı alanları,
-seçim kutuları,
-slider,
-progress bar

gibi arayüz elemanlarını burada tanımlanabilir.

### Ne zaman bu dosyaya bakmalıyım?

Yeni bir widget eklemek,mevcut bir widget'ı kaldırmak veya arayüzü değiştirmak istediğinizde bu dosyayı düzenleyebilirsiniz.

Örneğin yeni bir 'QPushButton'eklemek istiyorsunuz widget'ın arayüz tanımı burada bulunabilir.

---

## `institution_plugin_template_dialog.py`

Arayüzde bulunan widget'ların Python tarafındaki davranışlarının yazıldığı dosyadır.

Örneğin:

-butona basıldığında işlem yapmak,
-QLineEdit içerisindeki metni okumak,
-ComboBox seçimini almak,
-Slider değerini takip etmek,
-ProgressBar değerini değiştirmek

gibi işlemler burada yapılabilir.

Örneğin:

```python
self.pushButtonExample.clicked.connect(self.handle_button_click)
```

satırı bir butonun tıklama olayını Python fonksiyonuna bağlar.

Ardından:

```python
def handle_button_click(self):
    print("Button clicked")
```

şekilde butona basıldığında yapılacak işlem tanımlanabilir.

### Ne zaman bu dosyaya bakmalıyım?

Bir widget'ın **ne yapacağını**  değiştirmek istediğinizde bu dosyaya bakmalısınız.

Kısaca:

**Arayüzde ne görünecek? → `.ui` dosyası**

**Görünen şey ne yapacak? → `dialog.py` dosyası**

---

## `widgets/widget_examples.py`

Template içerisinde bulunan temel Qt widget'larının Python ile nasıl oluşturulabileceğini gösteren örnek dosyadır.

Örneğin:

```python
from qgis.PyQt.QtWidgets import QPushButton

button = QPushButton("Run")
```
Bu dosyanın amacı geliştiriciye hazır örnekler sağlamaktır.

Yeni bir plugin geliştirirken ihtiyacınız olan widget'ın nasıl oluşturulduğunu görmek için bu dosyada bakabilirsiniz.

---

## `widgets/README.md`

Template içerisinde bulunan widget örneklerinin açıklamalarını içerir.

Hangi widget'ın ne amaçla kullanılabileceğini hızlı şekilde görmek için kullanaılabilir.

## `KULLANIM_KILAVUZU.md`

Şu anda okuduğunuz ana Türkçe kullanım kılavuzudur.

Template'i daha önce hiç kullanmamış bir geliştiricinin:

-projeyi tanıması,
-dosyaların görevlerini öğrenmesi,
-yeni widget eklemesi,
-widget'ları Python koduna bağlaması,
-örnekleri kendi plugininde kullanması

için hazırlanmıştır.

---

# 4. Bir Değişiklik Yapmak İstediğimde Hangi Dosyaya Gitmeliyim?

Hızlı bir başlangıç için aşağıdaki mantık kullanılabilir.

| Yapmak istediğim işlem | Bakacağım yer |
|---|---|
| Plugin adını değiştirmek | `metadata.txt` |
| Plugin sürümünü değiştirmek | `metadata.txt` |
| Plugin ikonunu değiştirmek | `icon.png` |
| Yeni widget eklemek | `institution_plugin_template_dialog_base.ui` |
| Widget'ın ne yapacağını belirlemek | `institution_plugin_template_dialog.py` |
| Hazır widget örneği görmek | `widgets/widget_examples.py` |
| Widget hakkında açıklama okumak | `widgets/README.md` |
| Template'in nasıl kullanılacağını öğrenmek | `KULLANIM_KILAVUZU.md` |

# 5. Yeni Bir Widget Nasıl Eklenir?
Bu bölümde template içerisine yeni bir widget ekleme süreci adım adım anlatılmaktadır.

Bir widget eklerken iki temel dosya kullanılır:

1.`institution_plugin_template_dialog_base.ui`
   - Widget'ın arayüzde görünmesini sağlar.

2. `institution_plugin_template_dialog.py`
   - Widget'ın ne yapacağını tanımlar.

   Kısaca:

   **Widget'ı ekrana eklemek → `.ui` dosyası**

**Widget'a davranış kazandırmak → `dialog.py` dosyası**

---


## 5.1 QPushButton Ekleme Örneği

Örnek olarak yeni bir buton eklemek istediğimizi düşünelim.

Yeni butonun görevi ileride bir analiz işlemi başlatmak olsun.

### Adım 1 - Butonu Arayüze Ekle

`institution_plugin_template_dialog_base.ui` dosyasına aşağıdaki gibi bir buton eklenebilir:

```xml
<item>
 <widget class="QPushButton" name="runAnalysisButton">
  <property name="text">
   <string>Run Analysis</string>
  </property>
 </widget>
</item>
```

Burada:

```text
QPushButton
```

widget türüdür.

```text
runAnalysisButton
```

Python kodunda kullanacağımız `objectName` değeridir.

```text
Run Analysis
```

ise kullanıcının ekranda göreceği yazıdır.

---

### Adım 2 - Butonu Python Fonksiyonuna Bağla

`institution_plugin_template_dialog.py` dosyasında `__init__` fonksiyonu içerisinde:

```python
self.runAnalysisButton.clicked.connect(self.run_analysis)
```
satırı eklenebilir.

Bu satırın anlamı:

> Run Analysis butonuna tıklandığında `run_analysis` fonksiyonunu çalıştır.

---

### Adım 3 - Butonun Yapacağı İşlemi Yaz

Aynı class içerisinde:

```python
def run_analysis(self):
    print("Analysis started")
```

fonksiyonu oluşturulabilir.

Artık butona basıldığında:

```text
Analysis started
```

işlemi çalışacaktır.

Gerçek bir plugin içerisinde bu fonksiyonun içine kendi analiz kodunuz yazılabilir.

---

## 5.2 Hazır Bir Widget Örneğini Yeni Plugin İçin Kullanma

Template içerisinde bulunan örnek widget'ları tamamen sıfırdan yazmak zorunda değilsiniz.

Örneğin mevcut:

```python
self.pushButtonExample.clicked.connect(self.handle_button_click)
```

yapısını yeni bir plugin içerisinde:

```python
self.exportButton.clicked.connect(self.export_data)
```

şeklinde değiştirebilirsiniz.

Burada değiştirilen kısımlar:

Burada değiştirilen kısımlar:

```text
pushButtonExample
→ exportButton

handle_button_click
→ export_data
```

olmuştur.

Ardından:


```python
def export_data(self):
    print("Export started")
```

şeklinde kendi fonksiyonunuzu oluşturabilirsiniz.

---
## 5.3 Bir Widget'ı Çoğaltmak
Template içerisinde bir widget örneği bulunması yalnızca bir tane kullanılabileceği anlamına gelmez.

Örneğin iki farklı butona ihtiyaç varsa:

```text
[ Run Analysis ]
[ Clear Results ]
```

şeklinde iki 'QPushButton2 oluşturabilirsiniz.

Her widget için farklı bir 'objectName' kullanılmalıdır.

Örneğin:

```text
runAnalysisButton
clearResultsButton
```

Python tarafında:

```python
self.runAnalysisButton.clicked.connect(self.run_analysis)
self.clearResultsButton.clicked.connect(self.clear_results)
```

şeklinde ayrı fonksiyonlara bağlanabilir.

---

## 5.4 Kullanmadığım Widget'ı Silebilir miyim?

Evet.

Template içerisinde bulunan widget'ların hepsini kullanmak zorunda değilsiniz.

Örneğin yeni plugininizde 'QSlider' gerekmiyorsa ilgili widget'ı '.ui' dosyasından kaldırabilirsiniz.

Ancak widget'a ait Python kodu da bulunuyorsa ilgili bağlantıların da kaldırılması gerekir.

Örneğin '.ui' dosyasından:


```text
sliderExample
```

silinmişse Python tarafındaki:

```python
self.sliderExample.valueChanged.connect(self.update_slider_value)
```

satırı da kaldırılmalıdır.

Aksi durumda Python artık bulunmayan bir widget'a erişmeye çalışabilir.

---

# 6. Object Name Neden Önemlidir?
Her widget'ın Python kodundan erişebilmesi için benzersiz bir 'objectName' değreinin olması gerekir.

Örneğin:

'''text
runButton
fileButton
layerCombaBox
distanceSpinBox
outputTextEdit
'''

gibi isimler kullanılabilir.

İsimlerin widget'ın gerçek amacını açıklaması önerilir.

Örneğin:

```text
pushButton1
```

yerine:

```text
runAnalysisButton
```

daha anlaşılırdır.

Bu sayede kodu daha sonra okuyan bir geliştirici widget'ın ne amaçla kullanıldığını daha kolay anlayabilir.

# 7. Hazır Çalışan Örnekler

Template yalnızca widget'ların görünüşünü göstermez.

Bazı widget'lar gerçek davranış örnekleriyle birlikte hazırlanmıştır.

Bu örnekler yeni bir plugin geliştirirken doğrudan referans olarak kullanılabilir.

---

## 7.1 QPushButton Example

`QPushButton Example` basit bir buton tıklama örneğidir.

Butonun Python bağlantısı:

```python
self.pushButtonExample.clicked.connect(self.handle_button_click)
```

Butona tıklandığında çalışan fonksiyon:

```python
def handle_button_click(self):
    self.labelExample.setText(
        "Button clicked successfully."
    )
```

Bu örnek şunu gösterir:

```text
QPushButton
→ clicked sinyali
→ Python fonksiyonu
→ kullanıcıya sonuç gösterme
```

Yeni bir plugin içerisinde örneğin:

```python
self.saveButton.clicked.connect(self.save_data)
```
şeklinde değiştirilebilir.

---

## 7.2 Run Example

'Run Example' birden fazla widget içerisindekş değerin aynı anda nasıl okunabileceğini gösterir.

Örnekte bu widget'lardan veri alınmaktadır:

-QLineEdit
-QComboBox
-QCheckBox
-QRadioButton
-QSpinBox
-QDoubleSpinBox
-QSlider

Butona basıldığında bu değerler okunur ve QTextEdit içerisinde özet olarak gösterilir.

Örneğin:

'''text
Text:Example
ComboBox:Option 2
CheckBox:True
RadioButton:False 
SpinBox:25
DoubleSpinBox:2.5
Slider:60
'''
Bu yapı gerçek bir plugin içerisinde formdaki kullanıcı girdilerini toplamak için kullanılabilir.

---

## 7.3 Open File
'Open File' butonu kullanıcıdan bir dosya seçmesini ister.

Python tarafında 'QFileDialog' kullanılır:

```python
file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
    self,
    "Metin Dosyası Seç",
    "",
    "Text Files (*.txt);;All Files (*)"
)
```

Seçilen metin dosyasının içeriği Python ile okunur:

```python
with open(
    file_path,
    "r",
    encoding="utf-8",
    errors="replace"
) as file:
    content = file.read()
```

Daha sonra içerik QTextEdit içerisinde gösterilir:

```python
self.textEditExample.setPlainText(content)
```

Bu örnek şu akışı gösterir:

'''text
Open File 
-Dosya seç
-Dosya yolunu al
-Dosyayı oku
-İçeriği arayüzde göster

Gerçek bir plugin içerisinde aynı yöntem:

-veri dosyasını seçmek 
-konfigürasyon okumak
-metin dosyasını okumak
-çıktı dosyasını seçmek

gibi dosyalarda kullanılabilir.

---

## 7.4 Clear
'Clear' butonu birden fazla widget'ın tek bir fonksiyon içerisinden nasıl kontrol edebileceğini gösterir.

Örneğin:

```python
self.lineEditExample.clear()
self.textEditExample.clear()
self.comboBoxExample.setCurrentIndex(0)
self.checkBoxExample.setChecked(False)
self.radioButtonExample.setChecked(False)
self.spinBoxExample.setValue(0)
self.doubleSpinBoxExample.setValue(0.0)
self.sliderExample.setValue(0)
self.progressBarExample.setValue(0)
```

Bu örnek formu başlangıç dururmuna döndürür.

Yeni bir plugin içerisinde aynı yaklaşım:

```text
Reset
Clear Form
New Operation
Cancel Input
```

gibi işlermler için kullanılabilir.

---

## 7.5 QSlider

QSlider kullanıcın belirli bir aralık içerisinde değer seçmesini sağlar.

Mevcut template içerisinde slider değeri anlık olarak takip edilmektedir.

Bağlantı:

```python
self.sliderExample.valueChanged.connect(
    self.update_slider_value
)
```

Fonksiyon:

```python
def update_slider_value(self, value):
    self.sliderValueLabel.setText(
        f"Current Slider Value: {value}"
    )
```

Böylece kullanıcı slider'ı hareket ettirdiğinde seçilen değer anında ekranda görünür.

---

## 7.6 QProgressBar

QProgressBar kullanıcıdan veri almak için değil, bir işlemin ilerleme durumunu göstermek için kullanılır.

Template içerisinde slider ile progress bar arasında örnek bağlantı kurulmuştur:

```python
self.progressBarExample.setValue(value)
```

Bu nedenle:

```text
Slider = 25
→ ProgressBar = 25%

Slider = 80
→ ProgressBar = 80%
```

olur.

Gerçek bir plugin içerisinde progress bar örneğin:

Gerçek bir plugin içerisinde progress bar örneğin:

```text
Dosyalar işleniyor...
10%
35%
70%
100%
```

şeklinde uzun süren işlemleri göstermek için kullanılabilir.

---

# 8. Örnekleri Yeni Bir Plugin'de Nasıl Kullanırım?

Template içerisindeki örnekleri olduğu gibi kullanamak zorunda değilsiniz.

Genel yaklaşım:


```text
1. İhtiyacınız olan widget örneğini bulun.
2. Widget'ın objectName değerini kendi amacınıza göre değiştirin.
3. İlgili Python bağlantısını kopyalayın.
4. Fonksiyon adını kendi işleminize göre değiştirin.
5. Örnek davranış yerine kendi uygulama kodunuzu yazın.
6. Kullanmadığınız örnekleri kaldırın.
7. QGIS içerisinde tekrar test edin.
```

Örneğin template içerisinde:

```python
self.openFileButton.clicked.connect(self.open_file)
```

bulunmaktadır.

Yeni plugin içerisinde bunu:

```python
self.selectLayerButton.clicked.connect(
    self.select_layer_file
)
```

şeklinde değiştirebilirsiniz.

Ardından:

```python
def select_layer_file(self):
    # Plugin'e özel işlem burada yazılır.
    pass
```

şeklinde kendi davranışınızı oluşturabilirsiniz.

Template'in amacı geliştiriciye hazır bir başlangıç noktası vermektedir.

# 9. Ek Widget Örnekleri

Institution Plugin Template içerisinde temel widget örneklerine ek olarak daha gelişmiş widget örnekleri de bulunmaktadır.

Bu bölümde QListWidget,QTabWidget,QDateEdit,QTimeEdit,QGroupBox ve QTreeWidget örneklerinin ne işe yaradığı ve template içerisinde nasıl kullanıldığı açıklanmaktadır.

---

## 9.1 QListWidget

'QListWidget' , birden fazla öğeyi liste halinde göstermek ve kullanıcının bu öğeler arasından seçim yapmasını sağlamak için kullanılır.

Template içerisinde örnek olarak aşağıdaki öğeler bulunmaktadır:

```text
Buildings
Roads
Rivers
Parcels
```

QComboBox ile benzer şekilde seçim yapılmasını sağlar ancak QComboBox'tan farklı olarak seçenekler açılır bir menü içerisinde değil,doğrudan liste halinde görünür.

Pyton tarafında seçilen öğğeye şu şekilde erişilebilir.

```python
selected_list_item = self.listWidgetExample.currentItem()

if selected_list_item:
    list_value = selected_list_item.text()
else:
    list_value = "No selection"
```

Template içerisinde seçilen QListWidget değeri 'Run Example' butonuna basıldığında QTextEdit içerisinde gösterilmektedir.

Örneğin:

QGIS pluginlerinde QListWidget;

-katman listesi,
-doya listesi,
-işlem listesi,
-seçilebilir veri listesi

gibi amaçlarla kullanılabilir.

---

## 9.2 QTableWidget

'QTableWidget' , verileri satır ve sütunlardan oluşan tablo şeklinde göstermek için kullanılır.

Template içerisinde örnek olarak:

```text
Layer       Features
Buildings   125
Roads       340
Rivers      42
```

tablosu bulunmaktadır.

Tablodaki bri satıra tıklandığında o satırın bilgileri Python tarafından okunmaktadır.

Örneğin Roads satırına tıklandığında:


```text
Selected row: Roads - Features: 340
```
sonucu gösterilir.

Bunun için kullanılan örnek Python kodu:

```python
def handle_table_click(self, row, column):
    layer_item = self.tableWidgetExample.item(row, 0)
    features_item = self.tableWidgetExample.item(row, 1)

    if layer_item and features_item:
        self.labelExample.setText(
            f"Selected row: {layer_item.text()} - "
            f"Features: {features_item.text()}"
        )
```

Signal bağlantısı:

```python
self.tableWidgetExample.cellClicked.connect(
    self.handle_table_click
)
```

QGIS pluginlerinde QTableWidget;

- analiz sonuçları,
- katman bilgileri,
- öznitelik benzeri veriler,
- işlem sonuçları,
- rapor tabloları

gibi bilgileri göstermek için kullanılabilir.

---

## 9.3 QDateEdit

'QDataEdit' , kullanıcının tarih seçmesini sağlar.

Template içerisinde tarih:

```text
04.09.2026
```

formatında gösterilmektedir.

Takvim özelliği aktif olduğu için kullanıcı tarih alanındaki takvim düğmesine basarak tarih seçebilir.

Seçilen tarih Python tarafında şu şekilde alınmaktadır:

```python
selected_date = self.dateEditExample.date().toString(
    "dd.MM.yyyy"
)
```

'Run Example' butonuna basıldığında seçilne tarih QTextEdit içerisinde gösterilmektedir.

```text
DateEdit: 04.09.2026
```

QGIS pluginlerde QDateEdit;

-başlangıç tarihi,
-bitiş tarihi,
-veri tarihi,
-tarih filtresi,
-rapor tarihi

gibi alanlarda kullanılabilir.

---

## 9.4 QTimeEdit

'QTimeEdit',kullanıcının saat seçmesini sağlar.

Template içerisinde saat:

```text
14:30:00
```

formatımda gösterilmektedir.

Python tarafında seçilen saat:

```python
selected_time = self.timeEditExample.time().toString(
    "HH:mm:ss"
)
```

ile okunmaktadır.

'RunExample' butonuna basıldığında:


```text
TimeEdit: 14:30:00
```

şeklinde QTextEdit içerisinde gösterilmektedir.

QGIS pluginlerde QTimeEdit;

-işlem başlangıç saati,
-zaman filtresi,
-veri toplama saati,
-zaman tabanlı analizler

gibi işlememlerde kullanılabilir.

---

## 9.5 QGroupBox

'QGroupBox' , ilgili widget'ları aynı başlık altında görsel olarak gruplamak için kullanılır.

Template içerisinde örnek olarak:

Template içerisinde örnek olarak:

```text
QGroupBox Example - Analysis Settings

Related widgets can be grouped inside this area.

☐ Enable Example Setting
```

yapısı bulunmaktadır.

QGroupBox'ın temel amacı kullanıcıdan doğrudan veri almak değildir.

Arayüzde birbiriyle ilişkili widget'ların aynı bölüm altında düzenlenmesi sağlar.

Örneğin gerçek bir QGIS plugininde:


```text
Analysis Settings
    Distance
    Analysis Type
    Save Result
```

veya:

```text
Output Settings
    Output Folder
    File Format
    File Name
```

gibi gruplar oluşturulabilir.

---

## 9.6 QTreeWidget

'QTreeWidget' , hiyerarşik verileri ağaç yapısında göstermek için kullanılır.

Template içerisinde örnek olarak:

```text
▶ Layers
▶ Analysis
```

başlıkları bulunmaktadır.

'Layers' başlığının yanındaki küçük üçgene basıldığında alt öğeler açılır:

```text
▼ Layers
   Buildings
   Roads
   Rivers
```

`Analysis` açıldığında:

```text
▼ Analysis
   Buffer
   Clip
```

öğeleri görüntülenir.

Tekrar üçgene basıldığında ilgili bölüm kapanır.

### QTreeWidget ile QComboBox Arasındaki Fark

QComboBox genellikle tek seviyeli açılır liste şeklindedir:

```text
Option 1 ▼
```

QTreeWidget ise kategoriler ve alt kategoriler oluşturulabilir:

```text
▼ Layers
   Buildings
   Roads
   Rivers

▼ Analysis
   Buffer
   Clip
```

Bu nedenle QTreeWidget daha karmaşık ve hiyerarşik veriler için uygundur.

QGIS pluginlerde;

-katman grupları,
-analiz kategorileri,
-proje yapısı,
-dosya ağacı,
-işlem kategorileri

gibi alanlarda kullanılabilir.

---

# 10. QScrollArea Kullanımı

Template içerisinded çok sayıda widget örneği bulunmaktadır.

Widget sayısı arttığında bütün widget'ları aynı dialog penceresine yerleştirmek arayüzün sıkışmasına neden olabilir.

Örneğin;

-QGroupBox,
-QTreeWidget,
-QTableWidget,
-QListWidget

gibi yüksekliği daha fazla olan widget'lar eklendiğinde alt bölümlerdeki widget'lar birbirine çok yaklaşabilir veya görünüm bozulabilir.

Bu problemi çözmek için template içerisinde 'QScrollArea' kullanılmaktadır.

QScrollArea sayesinde kullanıcı pencere içerisinde aşağı ve yukarı kaydırma yapabilir.

Genel yapı:

```text
Dialog
│
├── QScrollArea
│   │
│   └── examplesLayout
│       ├── QLabel
│       ├── QPushButton
│       ├── QLineEdit
│       ├── QComboBox
│       ├── QCheckBox
│       ├── QRadioButton
│       ├── QSpinBox
│       ├── QDoubleSpinBox
│       ├── QSlider
│       ├── QProgressBar
│       ├── QTextEdit
│       ├── QListWidget
│       ├── QTableWidget
│       ├── QDateEdit
│       ├── QTimeEdit
│       ├── QGroupBox
│       └── QTreeWidget
│
└── QDialogButtonBox
    ├── OK
    └── Cancel
```

Bu yapıda örnek widget'lar kaydırılabilir alan içerisinde bulunur.

'OK' ve 'Cancel' butonları ise dialog penceresinin altında sabit kalabilir.

QScrollArea'nın kullanılmasının avantajları:

-Widget'ların birbirine girmesini engeller.
-Çok sayıda widget aynı dialog içerisinde kullanılabilir.
-Pencerenin gereksiz şekilde büyümesini engeller.
-Kullanıcı aşağı ve yukarı kaydırabilir.
-Template'e daha sonra yeni widget örnekleri eklemesini kolaylaştırır.

---

# 11. Hazır Buton Örnekleri

Template içerisinde yalnızca standart bir QPushButton değil, farklı işlemleri gösteren çeşitli buton örnekleri bulunmaktadır.

---

## 11.1 QPushButton Example

'QPushBuutton Example' , basit bir buton tıklama örneğidir.

Bağlantı:

```python
self.pushButtonExample.clicked.connect(
    self.handle_button_click
)
```

Butona basıldığında:

```text
Button clicked successfully.
```

mesajı gösterilir.

Bu örneğin amacı 'clicked' sinyalinin bir Python fonksiyonuna nasıl bağlandığını göstermektir.

---

## 11.2 Run Example

'Run Example' , birden fazla widget içerisindeki değerlerin aynı anda nasıl okunabileceğini gösterir.

Örneğin;

- QLineEdit,
- QComboBox,
- QCheckBox,
- QRadioButton,
- QSpinBox,
- QDoubleSpinBox,
- QSlider,
- QListWidget,
- QDateEdit,
- QTimeEdit

gibi widget'lardaki değerler Python tarafından okunabilir.

Sonuç QTextEdit içerisinde gösterilir.

Örneğin:

```text
Text: Example
ComboBox: Option 2
CheckBox: True
RadioButton: False
SpinBox: 25
DoubleSpinBox: 2.5
Slider: 60
ListWidget: Roads
DateEdit: 04.09.2026
TimeEdit: 14:30:00
```

Bu örnek gerçek bir plugin içerisinde form verilerinin nasıl toplanabileceğini göstermektedir.

---

## 11.3 Open File

`Open File` butonu kullanıcının bilgisayarından dosya seçmesini sağlar.

Template içerisinde QFileDialog kullanılmaktadır:

```python
file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
    self,
    "Metin Dosyası Seç",
    "",
    "Text Files (*.txt);;All Files (*)"
)
```

Dosya seçildikten sonra dosyanın içeriği okunur:

```python
with open(
    file_path,
    "r",
    encoding="utf-8",
    errors="replace"
) as file:
    content = file.read()
```

Sonuç QTextEdit içerisinde gösterilir:

```python
self.textEditExample.setPlainText(content)
```

Bu örnek;

```text
Dosya seç
      ↓
Dosya yolunu al
      ↓
Dosyayı Python ile oku
      ↓
İçeriği arayüzde göster
```

akışını göstermektedir.

---

## 11.4 Clear

`Clear` butonu formdaki widget'ları başlangıç durumuna döndürmek için kullanılmaktadır.

Örneğin:

```python
self.lineEditExample.clear()
self.textEditExample.clear()
self.comboBoxExample.setCurrentIndex(0)
self.checkBoxExample.setChecked(False)
self.radioButtonExample.setChecked(False)
self.spinBoxExample.setValue(0)
self.doubleSpinBoxExample.setValue(0.0)
self.sliderExample.setValue(0)
self.progressBarExample.setValue(0)
```

Bu örnek bir Python fonksiyonunun aynı anda birden fazla widget'ı nasıl kontrol edebileceğini göstermektedir.

Gerçek bir plugin içerisinde aynı yaklaşım;

- Clear Form,
- Reset,
- New Operation,
- Cancel Input

gibi işlemlerde kullanılabilir.

---

# 12. Widget Hızlı Referans Tablosu

| Widget | Kullanım Amacı |
|---|---|
| QLabel | Kullanıcıya metin veya sonuç göstermek |
| QLineEdit | Tek satırlık metin almak |
| QPushButton | Bir işlemi başlatmak |
| QComboBox | Açılır listeden seçim yaptırmak |
| QCheckBox | Bir özelliği açmak/kapatmak |
| QRadioButton | Seçenekler arasından seçim yaptırmak |
| QSpinBox | Tam sayı almak |
| QDoubleSpinBox | Ondalıklı sayı almak |
| QSlider | Bir aralıktan sürükleyerek değer seçmek |
| QProgressBar | İşlemin ilerleme durumunu göstermek |
| QTextEdit | Çok satırlı metin almak veya göstermek |
| QDialogButtonBox | OK/Cancel gibi standart dialog işlemlerini yönetmek |
| QListWidget | Öğeleri görünür liste halinde göstermek |
| QTableWidget | Satır ve sütun şeklinde veri göstermek |
| QDateEdit | Tarih seçmek |
| QTimeEdit | Saat seçmek |
| QGroupBox | İlgili widget'ları gruplamak |
| QTreeWidget | Hiyerarşik/açılır-kapanır veri göstermek |
| QFileDialog | Bilgisayardan dosya seçmek |
| QScrollArea | Çok sayıdaki widget'ı kaydırılabilir alanda göstermek |

---

# 13. Yeni Widget Eklerken Genel Yaklaşım

Template'e yeni bir widget eklemek için genel olarak iki bölüm üzerinde çalışılır:

```text
institution_plugin_template_dialog_base.ui
```

Arayüzde widget'ın görünümü burada tanımlanır.

```text
institution_plugin_template_dialog.py
```

Widget'ın Python davranışı burada tanımlanır.

Genel çalışma mantığı:

```text
.ui dosyasına widget ekle
        ↓
Widget'a objectName ver
        ↓
Python dosyasından objectName ile eriş
        ↓
Gerekirse signal bağlantısı oluştur
        ↓
Python fonksiyonu yaz
        ↓
QGIS içerisinde test et
```

Örneğin yeni bir buton:

```python
self.exampleButton.clicked.connect(
    self.example_function
)
```

ve fonksiyonu:

```python
def example_function(self):
    # Plugin'e özel işlem burada yapılır.
    pass
```

şeklinde oluşturulabilir.

Template içerisindeki widget'lar nihai bir uygulama oluşturmak için değil, yeni bir QGIS plugini geliştirirken örnek ve başlangıç noktası sağlamak için hazırlanmıştır.

Geliştirici ihtiyacı olmayan örnekleri kaldırabilir, mevcut örnekleri değiştirebilir veya aynı yapıyı kullanarak yeni widget ve davranışlar ekleyebilir.