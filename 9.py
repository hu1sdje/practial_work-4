ans_1 = input('Собака короткошерстной породы? ')
if ans_1 == 'да':
    ans_l2 = input('Рост собаки менее 50 см? ')
    if ans_l2 == 'да':
        ans_l3 = input('У собаки короткий хвост? ')
        if ans_l3 == 'да':
            print('английский бульдог')
        else:
            ans_l5 = input('У собаки длинные уши? ')
            if ans_l5 == 'да':
                print('гончая')
            else:
                ans_l6 = input('У собаки короткое тело? ')
                if ans_l6 == 'да':
                    print('мопс')
                else:
                    print('чихуахуа')
    else:
        ans_l4 = input('Собака весит более 50 кг? ')
        if ans_l4 == 'да':
            print('датский дог')
        else:
            print('фоксхаунд')
else:
    ans_r2 = input('Рост собаки менее 50 см? ')
    if ans_r2 == 'да':
        ans_r3 = input('У собаки доброжелательный характер? ')
        if ans_r3 == 'да':
            print('кокер-спаниель')
        else:
            print('ирландский сеттер')
    else:
        ans_r4 = input('У собаки рост менее 70 см?')
        if ans_r4 == 'да':
            ans_r5 = input('У собаки длинные уши? ')
            if ans_r5 == 'да':
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            ans_r6 = input('Окрас рыжий с белыми отметинами? ')
            if ans_r6 == 'да':
                print('сенбернар')
            else:
                ans_r7 = input('Белоснежный окрас? ')
                if ans_r7 == 'да':
                    print('сенбернар')
                else:
                    print('ньюфаундленд')
