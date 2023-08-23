from api.basic_methods import Api


class GetFoldersAndFiles(Api):
    def get_resources(
        self,
        path: str = None,
        fields: str = None,
        limit: str = None,
        offset: str = None,
        preview_crop: bool = None,
        preview_size: str = None,
        sort: str = None
    ):
        url = f"{self.url}/v1/disk/resources"
        return self.get(
            url=url,
            params={
                "path": path,
                "fields": fields,
                "limit": limit,
                "offset": offset,
                "preview_crop": preview_crop,
                "preview_size": preview_size,
                "sort": sort
            },
        )
