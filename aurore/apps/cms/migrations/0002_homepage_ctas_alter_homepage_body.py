# Generated by Django 4.1.2 on 2022-10-22 19:35

import aurore.apps.cms.blocks
from django.db import migrations
import wagtail.blocks
import wagtail.blocks.field_block
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="ctas",
            field=wagtail.fields.StreamField(
                [
                    (
                        "cta",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.blocks.CharBlock(
                                        default="Learn More",
                                        help_text="This is the text that appears on the link or button",
                                        max_length=40,
                                        required=True,
                                    ),
                                ),
                                (
                                    "link_url",
                                    wagtail.blocks.URLBlock(
                                        help_text="If the link page above is selected, that will be used first.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "open_in_new_tab",
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                help_text="The Call to Actions Buttons on your page",
                null=True,
                use_json_field=True,
                verbose_name="call of action",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "logos",
                        wagtail.blocks.ListBlock(
                            aurore.apps.cms.blocks.APIImageChooserBlock,
                            help_text="Add brand logos",
                            required=False,
                        ),
                    ),
                    (
                        "explore_section",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title_and_text",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(
                                                    help_text="Add your title",
                                                    required=True,
                                                ),
                                            ),
                                            (
                                                "text",
                                                wagtail.blocks.TextBlock(
                                                    help_text="Add subtitle or additional text",
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        help_text="Add your title and subtitle for the explore section",
                                        required=True,
                                    ),
                                ),
                                (
                                    "cards",
                                    wagtail.blocks.ListBlock(
                                        aurore.apps.cms.blocks.SimpleCardBlock,
                                        help_text="Add about cards",
                                        required=False,
                                    ),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                    (
                        "how_section",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title_and_text",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(
                                                    help_text="Add your title",
                                                    required=True,
                                                ),
                                            ),
                                            (
                                                "text",
                                                wagtail.blocks.TextBlock(
                                                    help_text="Add subtitle or additional text",
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        help_text="Add title and subtitle for this section",
                                        required=True,
                                    ),
                                ),
                                (
                                    "cards",
                                    wagtail.blocks.ListBlock(
                                        aurore.apps.cms.blocks.SimpleCardBlock,
                                        help_text="Add cards",
                                        required=False,
                                    ),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                    (
                        "project_section",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title_and_text",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(
                                                    help_text="Add your title",
                                                    required=True,
                                                ),
                                            ),
                                            (
                                                "text",
                                                wagtail.blocks.TextBlock(
                                                    help_text="Add subtitle or additional text",
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        help_text="Title and subtitle for project section",
                                        required=True,
                                    ),
                                ),
                                (
                                    "cards",
                                    wagtail.blocks.ListBlock(
                                        aurore.apps.cms.blocks.SimpleCardBlock,
                                        help_text="Add items",
                                        required=False,
                                    ),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                    (
                        "categories_section",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title_and_text",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(
                                                    help_text="Add your title",
                                                    required=True,
                                                ),
                                            ),
                                            (
                                                "text",
                                                wagtail.blocks.TextBlock(
                                                    help_text="Add subtitle or additional text",
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        help_text="Add your title and text",
                                        required=True,
                                    ),
                                ),
                                (
                                    "categories",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.field_block.CharBlock,
                                        help_text="Add categories",
                                        required=False,
                                    ),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                ],
                blank=True,
                use_json_field=True,
                verbose_name="content block",
            ),
        ),
    ]
