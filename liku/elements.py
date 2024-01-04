from abc import ABC, abstractmethod
import html as htmllib
from typing import Literal, TypedDict, overload, TypeAlias

from liku.signatures import (
    AnchorHTMLAttributes,
    AreaHTMLAttributes,
    AudioHTMLAttributes,
    BaseHTMLAttributes,
    BlockquoteHTMLAttributes,
    ButtonHTMLAttributes,
    CanvasHTMLAttributes,
    ColHTMLAttributes,
    ColgroupHTMLAttributes,
    DataHTMLAttributes,
    DelHTMLAttributes,
    DetailsHTMLAttributes,
    DialogHTMLAttributes,
    EmbedHTMLAttributes,
    FieldsetHTMLAttributes,
    FormHTMLAttributes,
    HTMLAttributes,
    HtmlHTMLAttributes,
    IframeHTMLAttributes,
    ImgHTMLAttributes,
    InputHTMLAttributes,
    InsHTMLAttributes,
    KeygenHTMLAttributes,
    LabelHTMLAttributes,
    LiHTMLAttributes,
    LinkHTMLAttributes,
    MapHTMLAttributes,
    MenuHTMLAttributes,
    MetaHTMLAttributes,
    MeterHTMLAttributes,
    ObjectHTMLAttributes,
    OlHTMLAttributes,
    OptgroupHTMLAttributes,
    OptionHTMLAttributes,
    OutputHTMLAttributes,
    ParamHTMLAttributes,
    ProgressHTMLAttributes,
    ScriptHTMLAttributes,
    SelectHTMLAttributes,
    SourceHTMLAttributes,
    StyleHTMLAttributes,
    TableHTMLAttributes,
    TdHTMLAttributes,
    TextareaHTMLAttributes,
    ThHTMLAttributes,
    TimeHTMLAttributes,
    TrackHTMLAttributes,
    VideoHTMLAttributes,
    WebViewHTMLAttributes,
)


class HTMLElement[PropsType: TypedDict](ABC):
    """Representation of a HTML element."""

    def __init__(
        self,
        props: PropsType | HTMLAttributes | dict[str, str] | None = None,
        children: "HTMLNode | None" = None,
        safe: bool = False,
    ):
        if not props:
            props = {}
        if not children:
            children = []

        if not isinstance(children, list):
            children = [children]

        self.props = props
        self.children = children
        self.safe = safe

    @abstractmethod
    def render(self) -> str:
        raise NotImplementedError

    def format_props(self):
        """Formats all props into html representation of them.

        Raises:
            TypeError: If the value of a prop is invalid.

        Returns:
            str: Formatted props to be used in HTML.
        """
        props = []
        for k, v in self.props.items():
            if isinstance(v, bool):
                v = str(v).lower()
            elif isinstance(v, int):
                v = str(v)

            if not isinstance(v, str):
                raise TypeError("Unexpected type for value:", type(v))

            v = htmllib.escape(v)
            if k.endswith("_"):
                k = k[:-1]
            props.append(f'{k}="{v}"')
        return " ".join(props)

    def render_child(self):
        """Renders all children of the element."""

        def _render(child: HTMLElement | str):
            if isinstance(child, HTMLElement):
                return child.render()

            if self.safe:
                return child
            return htmllib.escape(child)

        return "".join([_render(elem) for elem in self.children])

    def __str__(self):
        return self.render()

    def __repr__(self):
        return self.__str__()


class Fragment[PropsType: TypedDict](HTMLElement[PropsType]):
    def render(self):
        return self.render_child()


class GenericComponent[ElemPropsType: TypedDict]:
    """Wrapper for most web components to create class elements for each tag.

    Returns:
        type[HTMLElement[ElemPropsType]]: The generated class that can be used for
        representations of the element.
    """

    @staticmethod
    def create(tag_name: str) -> type[HTMLElement[ElemPropsType]]:
        """Creates a class for the given tag name.

        Args:
            tag_name (str): The name of the tag.

        Returns:
            type[HTMLElement[ElemPropsType]]: The generated class that can be used for
            representations of the element.
        """

        class Element(HTMLElement):
            def render(self):
                return f"<{tag_name} {self.format_props()}>{self.render_child()}</{tag_name}>"

        Element.__name__ = tag_name
        return Element


HTMLNode: TypeAlias = list[HTMLElement | str] | HTMLElement | str
a = GenericComponent[AnchorHTMLAttributes].create("a")
abbr = GenericComponent[HTMLAttributes].create("abbr")
address = GenericComponent[HTMLAttributes].create("address")
area = GenericComponent[AreaHTMLAttributes].create("area")
article = GenericComponent[HTMLAttributes].create("article")
aside = GenericComponent[HTMLAttributes].create("aside")
audio = GenericComponent[AudioHTMLAttributes].create("audio")
b = GenericComponent[HTMLAttributes].create("b")
base = GenericComponent[BaseHTMLAttributes].create("base")
bdi = GenericComponent[HTMLAttributes].create("bdi")
bdo = GenericComponent[HTMLAttributes].create("bdo")
big = GenericComponent[HTMLAttributes].create("big")
blockquote = GenericComponent[BlockquoteHTMLAttributes].create("blockquote")
body = GenericComponent[HTMLAttributes].create("body")
br = GenericComponent[HTMLAttributes].create("br")
button = GenericComponent[ButtonHTMLAttributes].create("button")
canvas = GenericComponent[CanvasHTMLAttributes].create("canvas")
caption = GenericComponent[HTMLAttributes].create("caption")
cite = GenericComponent[HTMLAttributes].create("cite")
code = GenericComponent[HTMLAttributes].create("code")
col = GenericComponent[ColHTMLAttributes].create("col")
colgroup = GenericComponent[ColgroupHTMLAttributes].create("colgroup")
data = GenericComponent[DataHTMLAttributes].create("data")
datalist = GenericComponent[HTMLAttributes].create("datalist")
dd = GenericComponent[HTMLAttributes].create("dd")
del_ = GenericComponent[DelHTMLAttributes].create("del")
details = GenericComponent[DetailsHTMLAttributes].create("details")
dfn = GenericComponent[HTMLAttributes].create("dfn")
dialog = GenericComponent[DialogHTMLAttributes].create("dialog")
div = GenericComponent[HTMLAttributes].create("div")
dl = GenericComponent[HTMLAttributes].create("dl")
dt = GenericComponent[HTMLAttributes].create("dt")
em = GenericComponent[HTMLAttributes].create("em")
embed = GenericComponent[EmbedHTMLAttributes].create("embed")
fieldset = GenericComponent[FieldsetHTMLAttributes].create("fieldset")
figcaption = GenericComponent[HTMLAttributes].create("figcaption")
figure = GenericComponent[HTMLAttributes].create("figure")
footer = GenericComponent[HTMLAttributes].create("footer")
form = GenericComponent[FormHTMLAttributes].create("form")
h1 = GenericComponent[HTMLAttributes].create("h1")
h2 = GenericComponent[HTMLAttributes].create("h2")
h3 = GenericComponent[HTMLAttributes].create("h3")
h4 = GenericComponent[HTMLAttributes].create("h4")
h5 = GenericComponent[HTMLAttributes].create("h5")
h6 = GenericComponent[HTMLAttributes].create("h6")
head = GenericComponent[HTMLAttributes].create("head")
header = GenericComponent[HTMLAttributes].create("header")
hgroup = GenericComponent[HTMLAttributes].create("hgroup")
hr = GenericComponent[HTMLAttributes].create("hr")
html = GenericComponent[HtmlHTMLAttributes].create("html")
i = GenericComponent[HTMLAttributes].create("i")
iframe = GenericComponent[IframeHTMLAttributes].create("iframe")
img = GenericComponent[ImgHTMLAttributes].create("img")
input = GenericComponent[InputHTMLAttributes].create("input")
ins = GenericComponent[InsHTMLAttributes].create("ins")
kbd = GenericComponent[HTMLAttributes].create("kbd")
keygen = GenericComponent[KeygenHTMLAttributes].create("keygen")
label = GenericComponent[LabelHTMLAttributes].create("label")
legend = GenericComponent[HTMLAttributes].create("legend")
li = GenericComponent[LiHTMLAttributes].create("li")
link = GenericComponent[LinkHTMLAttributes].create("link")
main = GenericComponent[HTMLAttributes].create("main")
map = GenericComponent[MapHTMLAttributes].create("map")
mark = GenericComponent[HTMLAttributes].create("mark")
menu = GenericComponent[MenuHTMLAttributes].create("menu")
menuitem = GenericComponent[HTMLAttributes].create("menuitem")
meta = GenericComponent[MetaHTMLAttributes].create("meta")
meter = GenericComponent[MeterHTMLAttributes].create("meter")
nav = GenericComponent[HTMLAttributes].create("nav")
noscript = GenericComponent[HTMLAttributes].create("noscript")
object = GenericComponent[ObjectHTMLAttributes].create("object")
ol = GenericComponent[OlHTMLAttributes].create("ol")
optgroup = GenericComponent[OptgroupHTMLAttributes].create("optgroup")
option = GenericComponent[OptionHTMLAttributes].create("option")
output = GenericComponent[OutputHTMLAttributes].create("output")
p = GenericComponent[HTMLAttributes].create("p")
param = GenericComponent[ParamHTMLAttributes].create("param")
picture = GenericComponent[HTMLAttributes].create("picture")
pre = GenericComponent[HTMLAttributes].create("pre")
progress = GenericComponent[ProgressHTMLAttributes].create("progress")
rp = GenericComponent[HTMLAttributes].create("rp")
rt = GenericComponent[HTMLAttributes].create("rt")
ruby = GenericComponent[HTMLAttributes].create("ruby")
s = GenericComponent[HTMLAttributes].create("s")
samp = GenericComponent[HTMLAttributes].create("samp")
script = GenericComponent[ScriptHTMLAttributes].create("script")
section = GenericComponent[HTMLAttributes].create("section")
select = GenericComponent[SelectHTMLAttributes].create("select")
small = GenericComponent[HTMLAttributes].create("small")
source = GenericComponent[SourceHTMLAttributes].create("source")
span = GenericComponent[HTMLAttributes].create("span")
strong = GenericComponent[HTMLAttributes].create("strong")
style = GenericComponent[StyleHTMLAttributes].create("style")
sub = GenericComponent[HTMLAttributes].create("sub")
summary = GenericComponent[HTMLAttributes].create("summary")
sup = GenericComponent[HTMLAttributes].create("sup")
table = GenericComponent[TableHTMLAttributes].create("table")
tbody = GenericComponent[HTMLAttributes].create("tbody")
td = GenericComponent[TdHTMLAttributes].create("td")
textarea = GenericComponent[TextareaHTMLAttributes].create("textarea")
tfoot = GenericComponent[HTMLAttributes].create("tfoot")
th = GenericComponent[ThHTMLAttributes].create("th")
thead = GenericComponent[HTMLAttributes].create("thead")
time = GenericComponent[TimeHTMLAttributes].create("time")
title = GenericComponent[HTMLAttributes].create("title")
tr = GenericComponent[HTMLAttributes].create("tr")
track = GenericComponent[TrackHTMLAttributes].create("track")
u = GenericComponent[HTMLAttributes].create("u")
ul = GenericComponent[HTMLAttributes].create("ul")
var = GenericComponent[HTMLAttributes].create("var")
video = GenericComponent[VideoHTMLAttributes].create("video")
wbr = GenericComponent[HTMLAttributes].create("wbr")
webview = GenericComponent[WebViewHTMLAttributes].create("webview")


@overload
def h(
    tag_name: Literal["a"],
    props: AnchorHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[AnchorHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["abbr"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["address"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["area"],
    props: AreaHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[AreaHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["article"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["aside"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["audio"],
    props: AudioHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[AudioHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["b"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["base"],
    props: BaseHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[BaseHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["bdi"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["bdo"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["big"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["blockquote"],
    props: BlockquoteHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[BlockquoteHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["body"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["br"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["button"],
    props: ButtonHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[ButtonHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["canvas"],
    props: CanvasHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[CanvasHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["caption"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["cite"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["code"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["col"],
    props: ColHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[ColHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["colgroup"],
    props: ColgroupHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[ColgroupHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["data"],
    props: DataHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[DataHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["datalist"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["dd"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["del_"],
    props: DelHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[DelHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["details"],
    props: DetailsHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[DetailsHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["dfn"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["dialog"],
    props: DialogHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[DialogHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["div"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["dl"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["dt"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["em"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["embed"],
    props: EmbedHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[EmbedHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["fieldset"],
    props: FieldsetHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[FieldsetHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["figcaption"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["figure"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["footer"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["form"],
    props: FormHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[FormHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["h1"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["h2"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["h3"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["h4"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["h5"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["h6"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["head"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["header"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["hgroup"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["hr"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["html"],
    props: HtmlHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HtmlHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["i"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["iframe"],
    props: IframeHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[IframeHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["img"],
    props: ImgHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[ImgHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["input"],
    props: InputHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[InputHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["ins"],
    props: InsHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[InsHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["kbd"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["keygen"],
    props: KeygenHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[KeygenHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["label"],
    props: LabelHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[LabelHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["legend"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["li"],
    props: LiHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[LiHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["link"],
    props: LinkHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[LinkHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["main"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["map"],
    props: MapHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[MapHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["mark"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["menu"],
    props: MenuHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[MenuHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["menuitem"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["meta"],
    props: MetaHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[MetaHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["meter"],
    props: MeterHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[MeterHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["nav"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["noscript"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["object"],
    props: ObjectHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[ObjectHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["ol"],
    props: OlHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[OlHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["optgroup"],
    props: OptgroupHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[OptgroupHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["option"],
    props: OptionHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[OptionHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["output"],
    props: OutputHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[OutputHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["p"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["param"],
    props: ParamHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[ParamHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["picture"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["pre"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["progress"],
    props: ProgressHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[ProgressHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["rp"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["rt"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["ruby"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["s"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["samp"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["script"],
    props: ScriptHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[ScriptHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["section"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["select"],
    props: SelectHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[SelectHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["small"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["source"],
    props: SourceHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[SourceHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["span"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["strong"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["style"],
    props: StyleHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[StyleHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["sub"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["summary"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["sup"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["table"],
    props: TableHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[TableHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["tbody"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["td"],
    props: TdHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[TdHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["textarea"],
    props: TextareaHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[TextareaHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["tfoot"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["th"],
    props: ThHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[ThHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["thead"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["time"],
    props: TimeHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[TimeHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["title"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["tr"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["track"],
    props: TrackHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[TrackHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["u"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["ul"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["var"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["video"],
    props: VideoHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[VideoHTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["wbr"],
    props: HTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[HTMLAttributes]:
    ...


@overload
def h(
    tag_name: Literal["webview"],
    props: WebViewHTMLAttributes | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[WebViewHTMLAttributes]:
    ...


def h[T: TypedDict](
    tag_name: str,
    props: T | dict[str, str] | None = None,
    children: list["HTMLElement | str"] | str | None = None,
    safe: bool = False,
) -> HTMLElement[T]:
    """Wrapper to create a component of given tag name, similar to JS ecosystem's `h()`.

    Returns:
        HTMLElement[T]: Created component
    """
    return GenericComponent.create(tag_name)(props, children, safe)
