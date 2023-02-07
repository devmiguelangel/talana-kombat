from rest_framework import serializers


class PlayerSerializer(serializers.Serializer):
    """ Player serializer """

    movimientos = serializers.ListField(
        child=(serializers.CharField(max_length=5, allow_blank=True))
    )
    golpes = serializers.ListField(
        child=(serializers.CharField(max_length=1, allow_blank=True))
    )

    def validate(self, data):
        if len(data['movimientos']) != len(data['golpes']):
            raise serializers.ValidationError('Moves and blows must have the same length')

        return data


class FightSerializer(serializers.Serializer):
    """ Fight serializer """

    player1 = PlayerSerializer()
    player2 = PlayerSerializer()
