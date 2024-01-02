# This file is completely translated from React's index.d.ts file
# https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/react/index.d.ts
#
# The conversion is done by AI, there might be some leftover changes made by React
# that is not consistent with HTML specification.
from typing import List, Literal, TypeAlias, Union, TypedDict

Any: TypeAlias = object
Booleanish: TypeAlias = Union[bool, str]


class AriaAttributes(TypedDict, total=True):
    aria_activedescendant: str
    aria_atomic: bool
    aria_autocomplete: str
    aria_braillelabel: str
    aria_brailleroledescription: str
    aria_busy: bool
    aria_checked: bool
    aria_colcount: int
    aria_colindex: int
    aria_colindextext: str
    aria_colspan: int
    aria_controls: str
    aria_current: bool
    aria_describedby: str
    aria_description: str
    aria_details: str
    aria_disabled: bool
    aria_dropeffect: str  # Deprecated in ARIA 1.1
    aria_errormessage: str
    aria_expanded: bool
    aria_flowto: str
    aria_grabbed: bool  # Deprecated in ARIA 1.1
    aria_haspopup: str
    aria_hidden: bool
    aria_invalid: bool
    aria_keyshortcuts: str
    aria_label: str
    aria_labelledby: str
    aria_level: int
    aria_live: str
    aria_modal: bool
    aria_multiline: bool
    aria_multiselectable: bool
    aria_orientation: str
    aria_owns: str
    aria_placeholder: str
    aria_posinset: int
    aria_pressed: bool
    aria_readonly: bool
    aria_relevant: str
    aria_required: bool
    aria_roledescription: str
    aria_rowcount: int
    aria_rowindex: int
    aria_rowindextext: str
    aria_rowspan: int
    aria_selected: bool
    aria_setsize: int
    aria_sort: str
    aria_valuemax: int
    aria_valuemin: int
    aria_valuenow: int
    aria_valuetext: str


AriaRole: TypeAlias = (
    Literal["alert"]
    | Literal["alertdialog"]
    | Literal["application"]
    | Literal["article"]
    | Literal["banner"]
    | Literal["button"]
    | Literal["cell"]
    | Literal["checkbox"]
    | Literal["columnheader"]
    | Literal["combobox"]
    | Literal["complementary"]
    | Literal["contentinfo"]
    | Literal["definition"]
    | Literal["dialog"]
    | Literal["directory"]
    | Literal["document"]
    | Literal["feed"]
    | Literal["figure"]
    | Literal["form"]
    | Literal["grid"]
    | Literal["gridcell"]
    | Literal["group"]
    | Literal["heading"]
    | Literal["img"]
    | Literal["link"]
    | Literal["list"]
    | Literal["listbox"]
    | Literal["listitem"]
    | Literal["log"]
    | Literal["main"]
    | Literal["marquee"]
    | Literal["math"]
    | Literal["menu"]
    | Literal["menubar"]
    | Literal["menuitem"]
    | Literal["menuitemcheckbox"]
    | Literal["menuitemradio"]
    | Literal["navigation"]
    | Literal["none"]
    | Literal["note"]
    | Literal["option"]
    | Literal["presentation"]
    | Literal["progressbar"]
    | Literal["radio"]
    | Literal["radiogroup"]
    | Literal["region"]
    | Literal["row"]
    | Literal["rowgroup"]
    | Literal["rowheader"]
    | Literal["scrollbar"]
    | Literal["search"]
    | Literal["searchbox"]
    | Literal["separator"]
    | Literal["slider"]
    | Literal["spinbutton"]
    | Literal["status"]
    | Literal["switch"]
    | Literal["tab"]
    | Literal["table"]
    | Literal["tablist"]
    | Literal["tabpanel"]
    | Literal["term"]
    | Literal["textbox"]
    | Literal["timer"]
    | Literal["toolbar"]
    | Literal["tooltip"]
    | Literal["tree"]
    | Literal["treegrid"]
    | Literal["treeitem"]
)


class HTMLAttributes(TypedDict, total=True):
    # Standard HTML Attributes
    accesskey: str
    autofocus: bool
    class_: str
    contenteditable: Union[Booleanish, Literal["inherit"], Literal["plaintext-only"]]
    contextmenu: str
    dir: str
    draggable: Booleanish
    hidden: bool
    id: str
    lang: str
    nonce: str
    slot: str
    spellcheck: Booleanish
    style: str
    tabindex: int
    title: str
    translate: Union[Literal["yes"], Literal["no"]]

    # Unknown
    radiogroup: str  # <command>, <menuitem>

    # WAI-ARIA
    role: AriaRole

    # RDFa Attributes
    about: str
    content: str
    datatype: str
    inlist: Any
    prefix: str
    property: str
    rel: str
    resource: str
    rev: str
    typeof: str
    vocab: str

    # Non-standard Attributes
    autocapitalize: str
    autocorrect: str
    autosave: str
    color: str
    itemprop: str
    itemscope: bool
    itemtype: str
    itemID: str
    itemref: str
    results: int
    security: str
    unselectable: Union[Literal["on"], Literal["off"]]

    # Living Standard
    inputmode: Literal[
        "none", "text", "tel", "url", "email", "numeric", "decimal", "search"
    ]
    is_: str  # 'is' is a reserved keyword, use 'is_' instead


# Define the CrossOrigin type for the 'crossOrigin' attribute
CrossOrigin = Literal["", "anonymous", "use-credentials"]

# Define the HTMLAttributeReferrerPolicy type
HTMLAttributeReferrerPolicy: TypeAlias = Literal[
    "",
    "no-referrer",
    "no-referrer-when-downgrade",
    "origin",
    "origin-when-cross-origin",
    "same-origin",
    "strict-origin",
    "strict-origin-when-cross-origin",
    "unsafe-url",
]


class AllHTMLAttributes(HTMLAttributes, total=True):
    # Standard HTML Attributes
    accept: str
    acceptcharset: str
    allowfullscreen: bool
    allowtransparency: bool
    alt: str
    as_: str  # 'as' is a reserved keyword, use 'as_' instead
    async_: bool
    autocomplete: str
    autoplay: bool
    capture: Union[bool, Literal["user", "environment"]]
    cellpadding: Union[int, str]
    cellspacing: Union[int, str]
    charset: str
    challenge: str
    checked: bool
    cite: str
    classID: str
    cols: int
    colspan: int
    controls: bool
    coords: str
    crossorigin: CrossOrigin
    data: str
    datetime: str
    default: bool
    defer: bool
    disabled: bool
    download: Any
    enctype: str
    form: str
    formenctype: str
    formmethod: str
    formnoValidate: bool
    formtarget: str
    frameborder: Union[int, str]
    headers: str
    height: Union[int, str]
    high: int
    href: str
    hreflang: str
    for_: str
    httpequiv: str
    integrity: str
    keyparams: str
    keytype: str
    kind: str
    label: str
    list: str
    loop: bool
    low: int
    manifest: str
    marginheight: int
    marginwidth: int
    max: Union[int, str]
    maxlength: int
    media: str
    mediagroup: str
    method: str
    min: Union[int, str]
    minlength: int
    multiple: bool
    muted: bool
    name: str
    novalidate: bool
    open: bool
    optimum: int
    pattern: str
    placeholder: str
    playsinline: bool
    poster: str
    preload: str
    readonly: bool
    required: bool
    reversed: bool
    rows: int
    rowspan: int
    sandbox: str
    scope: str
    scoped: bool
    scrolling: str
    seamless: bool
    selected: bool
    shape: str
    size: int
    sizes: str
    span: int
    src: str
    srcdoc: str
    srclang: str
    srcset: str
    start: int
    step: Union[int, str]
    summary: str
    target: str
    type: str
    usemap: str
    value: Union[str, List[str], int]
    width: Union[int, str]
    wmode: str
    wrap: str


# Define the HTMLAttributeAnchorTarget type
HTMLAttributeAnchorTarget: TypeAlias = (
    Literal["_self", "_blank", "_parent", "_top"] | str
)


class AnchorHTMLAttributes(HTMLAttributes, total=True):
    download: Any
    href: str
    hreflang: str
    media: str
    ping: str
    target: HTMLAttributeAnchorTarget
    type: str
    referrerpolicy: HTMLAttributeReferrerPolicy


class AudioHTMLAttributes(HTMLAttributes, total=True):
    pass


class AreaHTMLAttributes(HTMLAttributes, total=True):
    alt: str
    coords: str
    download: Any
    href: str
    hreflang: str
    media: str
    referrerpolicy: HTMLAttributeReferrerPolicy
    shape: str
    target: str


class BaseHTMLAttributes(HTMLAttributes, total=True):
    href: str
    target: str


class BlockquoteHTMLAttributes(HTMLAttributes, total=True):
    cite: str


class ButtonHTMLAttributes(HTMLAttributes, total=True):
    disabled: bool
    form: str
    formenctype: str
    formmethod: str
    formnovalidate: bool
    formtarget: str
    name: str
    type: Literal["submit", "reset", "button"]
    value: Union[str, List[str], int]


class CanvasHTMLAttributes(HTMLAttributes):
    height: Union[int, str]
    width: Union[int, str]


class ColHTMLAttributes(HTMLAttributes):
    span: int
    width: Union[int, str]


class ColgroupHTMLAttributes(HTMLAttributes):
    span: int


class DataHTMLAttributes(HTMLAttributes):
    value: Union[str, List[str], int]


class DetailsHTMLAttributes(HTMLAttributes):
    open: bool
    name: str


class DelHTMLAttributes(HTMLAttributes):
    cite: str
    datetime: str


class DialogHTMLAttributes(HTMLAttributes):
    open: bool


class EmbedHTMLAttributes(HTMLAttributes):
    height: Union[int, str]
    src: str
    type: str
    width: Union[int, str]


class FieldsetHTMLAttributes(HTMLAttributes):
    disabled: bool
    form: str
    name: str


class FormHTMLAttributes(HTMLAttributes):
    acceptcharset: str
    autocomplete: str
    enctype: str
    method: str
    name: str
    novalidate: bool
    target: str


class HtmlHTMLAttributes(HTMLAttributes):
    manifest: str


class IframeHTMLAttributes(HTMLAttributes):
    allow: str
    allowfullscreen: bool
    allowtransparency: bool
    frameborder: Union[int, str]
    height: Union[int, str]
    loading: Literal["eager", "lazy"]
    marginheight: int
    marginwidth: int
    name: str
    referrerpolicy: "HTMLAttributeReferrerPolicy"
    sandbox: str
    scrolling: str
    seamless: bool
    src: str
    srcdoc: str
    width: Union[int, str]


class ImgHTMLAttributes(HTMLAttributes):
    alt: str
    crossorigin: "CrossOrigin"
    decoding: Literal["async", "auto", "sync"]
    height: Union[int, str]
    loading: Literal["eager", "lazy"]
    referrerpolicy: "HTMLAttributeReferrerPolicy"
    sizes: str
    src: str
    srcset: str
    usemap: str
    width: Union[int, str]


class InsHTMLAttributes(HTMLAttributes):
    cite: str
    datetime: str


HTMLInputTypeAttribute = (
    Literal[
        "button",
        "checkbox",
        "color",
        "date",
        "datetime-local",
        "email",
        "file",
        "hidden",
        "image",
        "month",
        "number",
        "password",
        "radio",
        "range",
        "reset",
        "search",
        "submit",
        "tel",
        "text",
        "time",
        "url",
        "week",
    ]
    | str
)


class InputHTMLAttributes(HTMLAttributes):
    accept: str
    alt: str
    autocomplete: str
    capture: Union[bool, Literal["user", "environment"]]
    checked: bool
    disabled: bool
    enterkeyhint: Literal["enter", "done", "go", "next", "previous", "search", "send"]
    form: str
    formaction: str
    formenctype: str
    formmethod: str
    formnoValidate: bool
    formtarget: str
    height: Union[int, str]
    list: str
    max: Union[int, str]
    maxlength: int
    min: Union[int, str]
    minlength: int
    multiple: bool
    name: str
    pattern: str
    placeholder: str
    readonly: bool
    required: bool
    size: int
    src: str
    step: Union[int, str]
    type: HTMLInputTypeAttribute
    value: Union[str, List[str], int]
    width: Union[int, str]


class KeygenHTMLAttributes(HTMLAttributes):
    challenge: str
    disabled: bool
    form: str
    keytype: str
    keyparams: str
    name: str


class LabelHTMLAttributes(HTMLAttributes):
    form: str
    for_: str


class LiHTMLAttributes(HTMLAttributes):
    value: Union[str, List[str], int]


class LinkHTMLAttributes(HTMLAttributes):
    as_: str
    crossorigin: "CrossOrigin"
    fetchpriority: Literal["high", "low", "auto"]
    href: str
    hreflang: str
    integrity: str
    media: str
    imagesrcset: str
    imagesizes: str
    referrerpolicy: "HTMLAttributeReferrerPolicy"
    sizes: str
    type: str
    charset: str


class MapHTMLAttributes(HTMLAttributes):
    name: str


class MenuHTMLAttributes(HTMLAttributes):
    type: str


class MediaHTMLAttributes(HTMLAttributes):
    autoplay: bool
    controls: bool
    controlslist: str
    crossorigin: "CrossOrigin"
    loop: bool
    mediagroup: str
    muted: bool
    playsinline: bool
    preload: str
    src: str


class MetaHTMLAttributes(HTMLAttributes):
    charset: str
    httpequiv: str
    name: str
    media: str
    content: str


class MeterHTMLAttributes(HTMLAttributes):
    form: str
    high: int
    low: int
    max: Union[int, str]
    min: Union[int, str]
    optimum: int
    value: Union[str, List[str], int]


class QuoteHTMLAttributes(HTMLAttributes):
    cite: str


class ObjectHTMLAttributes(HTMLAttributes):
    classID: str
    data: str
    form: str
    height: Union[int, str]
    name: str
    type: str
    usemap: str
    width: Union[int, str]
    wmode: str


class OlHTMLAttributes(HTMLAttributes):
    reversed: bool
    start: int
    type: Literal["1", "a", "A", "i", "I"]


class OptgroupHTMLAttributes(HTMLAttributes):
    disabled: bool
    label: str


class OptionHTMLAttributes(HTMLAttributes):
    disabled: bool
    label: str
    selected: bool
    value: Union[str, List[str], int]


class OutputHTMLAttributes(HTMLAttributes):
    form: str
    for_: str
    name: str


class ParamHTMLAttributes(HTMLAttributes):
    name: str
    value: Union[str, List[str], int]


class ProgressHTMLAttributes(HTMLAttributes):
    max: Union[int, str]
    value: Union[str, List[str], int]


class SlotHTMLAttributes(HTMLAttributes):
    name: str


class ScriptHTMLAttributes(HTMLAttributes):
    async_: bool
    charset: str
    crossorigin: "CrossOrigin"
    defer: bool
    integrity: str
    nomodule: bool
    referrerpolicy: "HTMLAttributeReferrerPolicy"
    src: str
    type: str


class SelectHTMLAttributes(HTMLAttributes):
    autocomplete: str
    disabled: bool
    form: str
    multiple: bool
    name: str
    required: bool
    size: int
    value: Union[str, List[str], int]


class SourceHTMLAttributes(HTMLAttributes):
    height: Union[int, str]
    media: str
    sizes: str
    src: str
    srcset: str
    type: str
    width: Union[int, str]


class StyleHTMLAttributes(HTMLAttributes):
    media: str
    scoped: bool
    type: str


class TableHTMLAttributes(HTMLAttributes):
    align: Literal["left", "center", "right"]
    bgcolor: str
    border: int
    cellpadding: Union[int, str]
    cellspacing: Union[int, str]
    frame: bool
    rules: Literal["none", "groups", "rows", "columns", "all"]
    summary: str
    width: Union[int, str]


class TextareaHTMLAttributes(HTMLAttributes):
    autocomplete: str
    cols: int
    dirname: str
    disabled: bool
    form: str
    maxlength: int
    minlength: int
    name: str
    placeholder: str
    readonly: bool
    required: bool
    rows: int
    value: Union[str, List[str], int]
    wrap: str


class TdHTMLAttributes(HTMLAttributes):
    align: Literal["left", "center", "right", "justify", "char"]
    colspan: int
    headers: str
    rowspan: int
    scope: str
    abbr: str
    height: Union[int, str]
    width: Union[int, str]
    valign: Literal["top", "middle", "bottom", "baseline"]


class ThHTMLAttributes(HTMLAttributes):
    align: Literal["left", "center", "right", "justify", "char"]
    colspan: int
    headers: str
    rowspan: int
    scope: str
    abbr: str


class TimeHTMLAttributes(HTMLAttributes):
    datetime: str


class TrackHTMLAttributes(HTMLAttributes):
    default: bool
    kind: str
    label: str
    src: str
    srclang: str


class VideoHTMLAttributes(MediaHTMLAttributes):
    height: Union[int, str]
    playsinline: bool
    poster: str
    width: Union[int, str]
    disablepictureinpicture: bool
    disableremoteplayback: bool


class WebViewHTMLAttributes(HTMLAttributes):
    allowfullscreen: bool
    allowpopups: bool
    autosize: bool
    blinkfeatures: str
    disableblinkfeatures: str
    disableguestresize: bool
    disablewebsecurity: bool
    guestinstance: str
    httpreferrer: str
    nodeintegration: bool
    partition: str
    plugins: bool
    preload: str
    src: str
    useragent: str
    webpreferences: str
