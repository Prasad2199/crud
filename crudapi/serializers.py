from rest_framework  import serializers
class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    img = serializers.ImageField()
    summary = serializers.CharField(max_length=500)

    def Create(self, validated_data):
        return Person.objects.Create(**validated_data)
    
    def update(self,instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.name=validated_data.get('img',instance.img)
        instance.name=validated_data.get('summary',instance.summary)
        instance.save()
        return instance
    