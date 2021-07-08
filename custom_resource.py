import pulumi.dynamic

class CustomDynamicResourceProvider(
    pulumi.dynamic.ResourceProvider,
):
    pass


pulumi.dynamic.Resource(
    provider=CustomDynamicResourceProvider(),
    name='my-resource',
    props={},
)
