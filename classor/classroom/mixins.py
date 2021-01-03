

class FieldsMixin():
    def dispatch(self,request, *args, **kwargs):
        teacher= profile.limit_choices_to={'role': 2}
        if request.profile.role==2 :
            self.fields = ["classworks_body","classworks_name"]

        return super().dispatch(request, *args, **kwargs)
