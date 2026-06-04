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

        user3 = User.objects.create_user(
            email="carla.ribeiro@example.com",
            username="user3",
            password="1234",
            first_name="Carla",
            last_name="Ribeiro",
            celular="11977777777",
            cidade="Campinas",
            estado="SP",
        )

        user4 = User.objects.create_user(
            email="rafael.costa@example.com",
            username="user4",
            password="1234",
            first_name="Rafael",
            last_name="Costa",
            celular="31966666666",
            cidade="Belo Horizonte",
            estado="MG",
        )

        user5 = User.objects.create_user(
            email="aline.martins@example.com",
            username="user5",
            password="1234",
            first_name="Aline",
            last_name="Martins",
            celular="51955555555",
            cidade="Porto Alegre",
            estado="RS",
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

        pet4 = Pet.objects.create(
            nome="Pingo",
            especie="Cachorro",
            raca="SRD",
            idade=1,
            porte="pequeno",
            descricao="Filhote curioso e animado, gosta de passeios curtos e colo.",
            vacinado=False,
            castrado=False,
            dono=user3,
        )

        pet5 = Pet.objects.create(
            nome="Pietro",
            especie="Cachorro",
            raca="SRD",
            idade=6,
            porte="médio",
            descricao="Cão tranquilo e observador, já aprendeu comandos básicos e adora rotina.",
            vacinado=True,
            castrado=True,
            dono=user4,
        )

        pet6 = Pet.objects.create(
            nome="Duque",
            especie="Cachorro",
            raca="SRD",
            idade=7,
            porte="grande",
            descricao="Companheiro leal que se dá bem com adultos e ambientes calmos.",
            vacinado=True,
            castrado=True,
            dono=user5,
        )

        pet7 = Pet.objects.create(
            nome="Mike",
            especie="Cachorro",
            raca="SRD",
            idade=4,
            porte="médio",
            descricao="Brincalhão e sociável, gosta de brinquedos e de companhia constante.",
            vacinado=True,
            castrado=False,
            dono=user3,
        )

        pet8 = Pet.objects.create(
            nome="Zara",
            especie="Gato",
            raca="SRD",
            idade=3,
            porte="pequeno",
            descricao="Gata independente, mas muito carinhosa depois que ganha confiança.",
            vacinado=True,
            castrado=True,
            dono=user4,
        )

        pet9 = Pet.objects.create(
            nome="Francisco",
            especie="Gato",
            raca="SRD",
            idade=5,
            porte="pequeno",
            descricao="Gato calmo e adaptável, ótimo para quem busca um companheiro sereno.",
            vacinado=False,
            castrado=True,
            dono=user5,
        )

        pet10 = Pet.objects.create(
            nome="Felix",
            especie="Gato",
            raca="SRD",
            idade=5,
            porte="pequeno",
            descricao="Um gato alegre e brincalhão, adora interagir com pessoas e outros animais, perfeito para famílias ativas.",
            vacinado=False,
            castrado=True,
            dono=user1,
        )

        FotoPet.objects.create(pet=pet1, imagem="/pets/cao-leo.jpeg")
        FotoPet.objects.create(pet=pet2, imagem="/pets/gato-maia.jpg")
        FotoPet.objects.create(pet=pet3, imagem="/pets/cao-luna.jpeg")
        FotoPet.objects.create(pet=pet4, imagem="/pets/cao-pingo.jpg")
        FotoPet.objects.create(pet=pet5, imagem="/pets/cao-pietro.jpg")
        FotoPet.objects.create(pet=pet6, imagem="/pets/cao-duque.jpg")
        FotoPet.objects.create(pet=pet7, imagem="/pets/cao-mike.jpg")
        FotoPet.objects.create(pet=pet7, imagem="/pets/cao-mike-2.jpg")
        FotoPet.objects.create(pet=pet8, imagem="/pets/gato-zara.jpg")
        FotoPet.objects.create(pet=pet8, imagem="/pets/gato-zara-2.jpg")
        FotoPet.objects.create(pet=pet9, imagem="/pets/gato-francisco.jpg")

        PedidoAdocao.objects.create(pet=pet1, adotante=user2)
        PedidoAdocao.objects.create(pet=pet2, adotante=user1)
        PedidoAdocao.objects.create(pet=pet4, adotante=user2)
        PedidoAdocao.objects.create(pet=pet5, adotante=user1)
        PedidoAdocao.objects.create(pet=pet7, adotante=user4, status="aprovado")
        PedidoAdocao.objects.create(pet=pet8, adotante=user1, status="rejeitado")
        PedidoAdocao.objects.create(pet=pet9, adotante=user2)

        self.stdout.write(self.style.SUCCESS("Dados de exemplo criados com sucesso!"))
