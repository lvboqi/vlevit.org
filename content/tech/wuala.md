/title: Wuala - бэкап, синхронизация, расшаривание
/created: 2011-04-22 23:31+03:00
/tags: wuala, бэкап, синхронизация, p2p, файлообмен

[TOC]

## В поисках...

Очень многие люди сталкиваются с необходимостью резервного копирования
данных. Один из первых вопросов, которым они задаются — это куда
копировать. Копировать можно на другой жесткий диск (плохо), выносной
жесткий диск (чуть лучше), на другой компьютер в том же помещении (еще
немного лучше), на другой географически отдаленный компьютер (хорошо,
если он легко доступен), а еще лучше – на несколько таких
компьютеров. За деньги такую услугу вам могут предоставить несчетное
количество компаний. Одно дело, если это нужно для бизнеса, другое
дело — если это личные данные пользователей, которых сотни
миллионов[^1]. Почему бы не хранить данные на машинах других
пользователей? Услуга за услугу — я храню свои данные на их
компьютерах, а они свои — на моем.

Я немного заинтересовавшись данной темой, пытался найти готовые
функционирующие решения p2p-бэкапа данных, не требующих поднятия
серверов работающих 24 часа в сутки или что-то в этом духе . Нашел
пару программ, не особо пользующихся популярностью. Одним из таких
было решение, смысл которого в следующем: ваши данные шифруются и
хранятся на компьютерах ваших друзей (или кого вы укажите), а те могут
столько же по объему хранить на вашем компьютере (или больше с вашего
позволения). Копии данных можно хранить сразу на нескольких
компьютерах, но в таком случае нужно выделять и у себя больше
пространства. Доступность данных зависит, от того, насколько у вас
хорошие друзья. Еще один минус — вам придется уговаривать друзей
делать то, чего они не хотят или не понимают. А если даже хотят, то
ваши потребности должны примерно совпадать (у одного потребность в
бэкапе может быть 10МБ, у другого — 10ГБ). Короче, схема в большинстве
случаев нежизнеспособна.

Решением может быть использование глобальных распределенных
отказоустойчивых файловых систем (или сетей), которые прибегают к
созданию избыточных данных для гарантий их доступности с высокой
вероятностью (например 99,9%), несмотря на то, что сами участники сети
могут отключаться, когда угодно. Первое, что я нашел и попробовал —
Freenet. Работает очень туго даже с настройками наименьшей
анонимности. Бекап данных по сути невозможен[^2]. Затем я узнал о
GNUnet и Wuala. С GNUnet я мало экспериментировал, но по первым
впечатлениям возможность приспособления сервиса для целей резервного
хранения я полностью не исключил. Wuala — коммерческий проект, от
сервиса которого я получил все, что хотел. Даже немного больше.

[^1]: Количество людей в сотни миллионов, которым нужен бэкап данных,
это всего лишь мое предположение (исходя из числа в два миллиарда
интернет-пользователей), которое применено образно...
[^2]: Справедливости ради следует заметить, что резервное хранение
данных — далеко от основной цели проекта Freenet.


## Wuala

О технических деталях, как эта p2p-сеть организована и работает, можно
узнать из [этого видео]. Я же расскажу об основных условиях
использования и возможностях сервиса.

После регистрации на сайте [www.wuala.com], вам предоставляется 1 ГБ
пространства или 2 ГБ по инвайту (например, [моему]). Чтобы получить
больше, вы приглашаете новых участников, покупаете дисковое
пространство за деньги, или торгуете своим дисковым
пространством. Если вы решили торговать, то находясь в сети постоянно,
вам выделяется столько же места, сколько вы выделите на своем жестком
диске. Если же меньше, то вам предоставляется объем, равный
произведению вашей доступности на объем вами выделенного
пространства. Например, я в среднем нахожусь 50% времени в сети и
выделил 20 ГБ пространства, поэтому получаю 0.5 • 20 = 10 ГБ (не
считая подаренный гигабайт при регистрации и заработанные на
приглашениях).

Помимо возможности бесплатно получить почти любое пространство,
торгуя своим, Wuala выделяет еще одно огромное преимущество среди
всяких дропбоксов: все данные шифруются на вашем компьютере, ключ
хранится (если вы не вводите пароль каждый раз вручную) на вашем
компьютере. Доступ к приватным данным из браузера поэтому невозможен,
как в других сервисах — для этого необходимо запускать клиент.

Торгуя дисковым пространством, пользователь становится Pro User'ом,
которому становятся доступны функции синхронизации, бекапа, и простой
версионной системы. Клиенты Wuala существуют для Linux, Mac, Windows,
iOS, в скором будущем обещают и для Android. Интеграция с файловой
системой осуществляется посредством FUSE для Linux и Mac, Dokan для
Windows. Клиент написан на Java. Доступно два режима запуска клиента:
в режиме демона и с графическим интерфейсом. Клиент в графическом
режиме у меня занимает 60+МБ и что-то около 30МБ в режиме демона
(примерно столько же, сколько и Dropbox). К сожалению, командный
интерфейс неполнофункциональный, и некоторые операции можно выполнить
только из графического интерфейса. Тем мене, в планах у них [есть]
создание API, с помощью которого можно будет получить доступ ко всем
функциям. [Существует] и RESTful API, которое поддерживает только
GET-запросы.

Из других особенностей. Wuala обладает достаточно гибким управлением
правами доступа. Отдельные каталоги (и подкаталоги) можно оставлять
приватным, делать публичными, делать доступными по ссылке, содержащей
в себе ключ, делать видимыми только для указанных пользователей или
групп Wuala. Также можно создавать полноценные публичные и приватные
группы. Можно устанавливать права каждого члена группы, назначать
модераторов и администраторов. Группы не имеют ограничений на размер.
Объем, занимаемый файлами, высчитывается из тех членов группы,
владельцами которых они являются. Данные кешируются, размер кеша
выставляется, поэтому часто обращение к файлами в ~/WualaDrive также
быстро как к локальным. Клиент поддерживает комментарии к файлам,
миниатюры изображений, оповещения при изменении/добавлении новых
файлов.

Насколько в режиме ожидания Wuala грузит канал? Привычная картина у
меня — 0КБ/с в обе стороны. Загрузка и аплоад производятся достаточно
быстро, скорее всего, потому что данные загружаются сначала на сервера
Wuala, а потом уже на машины пользователей.

Если подытожить, сервис Wuala обладает следующими преимуществами
над конкурирующими сервисами:

  * торговля дисковым пространством;
  * шифрование на стороне пользователя;
  * гибкий контроль прав доступа и поддержка полноценных групп.

И обладает следующими недостатками:

  * закрытый java-клиент (в принципе, почти все клиенты подобных
    сервисов закрытые);
  * неполнофункциональный командный интерфейс.

[этого видео]: http://www.youtube.com/watch%3Fv%3D3xKZ4KGkQY8
[www.wuala.com]: http://www.wuala.com
[моему]: http://www.wuala.com/referral/ANKKPB4J3HH3BB6G77MB
[есть]: http://bugs.wuala.com/view.php%3Fid%3D2964
[Существует]: http://www.wuala.com/en/api
