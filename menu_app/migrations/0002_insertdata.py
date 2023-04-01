from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO menu_app_category (id, name, names) 
                VALUES (1, 'main_menu', 'Main menu');

            INSERT INTO menu_app_menu (id, name, path, category_id, parent_id) 
                VALUES (1, 'Главная страница', 'index', 1, null);
            INSERT INTO menu_app_menu (id, name, path, category_id, parent_id) 
                VALUES (2, 'Магазин', 'store', 1, null);
            INSERT INTO menu_app_menu (id, name, path, category_id, parent_id) 
                VALUES (3, 'Все товары', 'goods', 1, null);
            INSERT INTO menu_app_menu (id, name, path, category_id, parent_id) 
                VALUES (4, 'Обувь', 'goods_shoes', 1, 3);
            INSERT INTO menu_app_menu (id, name, path, category_id, parent_id) 
                VALUES (5, 'Спортивная обувь', 'goods_sport_shoes', 1, 4);
            INSERT INTO menu_app_menu (id, name, path, category_id, parent_id) 
                VALUES (6, 'Одежда', 'goods_cloth', 1, 3);
            INSERT INTO menu_app_menu (id, name, path, category_id, parent_id) 
                VALUES (7, 'Рубашки', 'goods_cloth_shirt', 1, 6);
            INSERT INTO menu_app_menu (id, name, path, category_id, parent_id) 
                VALUES (8, 'Брюки', 'goods_cloth_trousers', 1, 6);
            INSERT INTO menu_app_menu (id, name, path, category_id, parent_id) 
                VALUES (9, 'Цены', 'prices', 1, null);
            INSERT INTO menu_app_menu (id, name, path, category_id, parent_id) 
                VALUES (10, 'Аксессуары', 'accessories', 1, 3);
            INSERT INTO menu_app_menu (id, name, path, category_id, parent_id) 
                VALUES (11, 'Туфли', 'goods_classic_shoes', 1, 4);
            
        """)
    ]