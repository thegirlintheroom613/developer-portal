# Generated by Django 2.2.3 on 2019-07-23 15:43

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('externalcontent', '0008_externalcontent_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalArticleAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('article', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='externalcontent.ExternalArticle')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='external_articles', to='people.Person')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]