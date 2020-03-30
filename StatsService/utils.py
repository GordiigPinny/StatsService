class RetrieveQueryParamsMixin:
    """
    Миксина для вытягивания query-params и формирования lookup_fields
    """
    def get_lookup_fields(self, params_list=None):
        params_list = params_list or ['user_id', 'place_id']
        ans = {}
        for param in params_list:
            try:
                ans[param] = self.request.query_params[param]
            except KeyError:
                pass
        return ans
