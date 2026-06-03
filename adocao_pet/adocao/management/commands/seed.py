from django.core.management.base import BaseCommand, CommandParser

from adocao.models import Pet, FotoPet, User, PedidoAdocao


class Command(BaseCommand):
    help = "Popula o banco de dados com dados de exemplo para desenvolvimento e testes."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Limpa os dados existentes antes de criar os dados de exemplo.",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            User.objects.all().delete()
            Pet.objects.all().delete()
            FotoPet.objects.all().delete()
            PedidoAdocao.objects.all().delete()

        user1 = User.objects.create_user(
            email="joao.silva@example.com",
            username="user1",
            password="1234",
            first_name="João",
            last_name="Silva",
            celular="11999999999",
            cidade="São Paulo",
            estado="SP",
        )

        user2 = User.objects.create_user(
            email="maria.souza@example.com",
            username="user2",
            password="1234",
            first_name="Maria",
            last_name="Souza",
            celular="11988888888",
            cidade="Rio de Janeiro",
            estado="RJ",
        )

        User.objects.create_superuser(
            username="admin",
            password="1234",
            first_name="Admin",
            email="admin@example.com",
        )

        pet1 = Pet.objects.create(
            nome="Léo",
            especie="Cachorro",
            raca="SRD",
            idade=3,
            porte="médio",
            descricao="Um cachorro amigável e brincalhão, adora crianças e é ótimo para famílias.",
            vacinado=True,
            castrado=True,
            dono=user1,
        )

        pet2 = Pet.objects.create(
            nome="Maia",
            especie="Gato",
            raca="SRD",
            idade=2,
            porte="pequeno",
            descricao="Uma gata gentil e curiosa, adora brincar e é perfeita para casas com espaço.",
            vacinado=True,
            castrado=True,
            dono=user2,
        )

        pet3 = Pet.objects.create(
            nome="Luna",
            especie="Cachorro",
            raca="SRD",
            idade=4,
            porte="grande",
            descricao="Leal e amorosa, adora atividades ao ar livre e é ótima para famílias ativas.",
            vacinado=True,
            castrado=True,
            dono=user1,
        )

        FotoPet.objects.create(pet=pet1, imagem="adocao_pet/seed/images/cao-leo.jpeg")
        FotoPet.objects.create(pet=pet2, imagem="adocao_pet/seed/images/gato-maia.jpeg")
        FotoPet.objects.create(pet=pet3, imagem="adocao_pet/seed/images/cao-luna.jpeg")

        PedidoAdocao.objects.create(pet=pet1, adotante=user2)
        PedidoAdocao.objects.create(pet=pet2, adotante=user1)

        self.stdout.write(self.style.SUCCESS("Dados de exemplo criados com sucesso!"))
