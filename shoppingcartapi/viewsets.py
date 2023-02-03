from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin


class CommonModelViewSet(
    CreateModelMixin, 
    UpdateModelMixin, 
    ListModelMixin, 
    RetrieveModelMixin,
    DestroyModelMixin,
):
    pass
