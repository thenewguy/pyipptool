from deform.widget import MappingWidget, SequenceWidget, Widget
import colander


class IPPDisplayWidget(Widget):
    def serialize(self, field, cstruct=None, readonly=False):
        return 'DISPLAY {}'.format(field.name.replace('_', '-'))


class IPPNameWidget(Widget):
    def serialize(self, field, cstruct=None, readonly=False):
        name = field.name
        while field.parent is not None:
            field = field.parent
        value = getattr(field.schema, name)
        return '{} "{}"'.format(field.name.upper(), value)


class IPPGroupWidget(Widget):
    def serialize(self, field, cstruct=None, readonly=False):
        name = field.name
        while field.parent is not None:
            field = field.parent
        value = getattr(field.schema, name)
        return 'GROUP {}'.format(value)


class IPPAttributeWidget(Widget):
    def serialize(self, field, cstruct=None, readonly=False):
        if cstruct is colander.null:
            return ''
        return 'ATTR {attr_type} {attr_name} {attr_value}'.format(
            attr_type=field.schema.typ.__class__.__name__.lower(),
            attr_name=field.name.replace('_', '-'),
            attr_value=cstruct)


class IPPBodyWidget(MappingWidget):
    readonly_template = 'ipp/form'
    template = readonly_template
    item_template = 'ipp/item'


class IPPTupleWidget(SequenceWidget):
    readonly_template = 'ipp/tuple'
    template = readonly_template
    item_template = 'ipp/item'


class IPPConstantTupleWidget(SequenceWidget):
    readonly_template = 'ipp/constant_tuple'
    template = readonly_template
    item_template = 'ipp/item'