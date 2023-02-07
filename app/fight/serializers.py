from rest_framework import serializers


class PlayerSerializer(serializers.Serializer):
    """ Player serializer """

    movimientos = serializers.ListField(
        child=(serializers.CharField(max_length=5, allow_blank=True))
    )
    golpes = serializers.ListField(
        child=(serializers.CharField(max_length=1, allow_blank=True))
    )

    def validate_movimientos(self, value):
        for m in value:
            if len(m) > 0:
                moves = [*m]

                if not set(moves).issubset(['W', 'S', 'A', 'D']):
                    raise serializers.ValidationError('Moves are not in validated keys')

        return value

    def validate_golpes(self, value):
        for b in value:
            if len(b) > 0 and b not in ['P', 'K']:
                raise serializers.ValidationError('Bowls are not in validated keys')

        return value

    def validate(self, data):
        if len(data['movimientos']) != len(data['golpes']):
            raise serializers.ValidationError('Moves and blows must have the same length')

        return data


class FightSerializer(serializers.Serializer):
    """ Fight serializer """

    player1 = PlayerSerializer()
    player2 = PlayerSerializer()
