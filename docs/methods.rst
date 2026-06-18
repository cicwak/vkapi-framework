Методы VK API
=============

Эта страница описывает методы, которые доступны в текущей сборке ``vkapi``.
Список ниже построен по ``src/vkapi/methods/generated.py``: сейчас в SDK есть
``569`` типизированных методов в ``44`` группах.

Сами классы методов генерируются из официальной схемы `VKCOM/vk-api-schema <https://github.com/VKCOM/vk-api-schema>`__.
Ссылки ведут в официальную документацию VK по шаблону ``https://dev.vk.com/method/<method>``.

Способы вызова
-------------------------

Основной вариант: вызывать метод через namespace на объекте ``Bot``. Имя namespace
совпадает с частью метода до точки, а имя функции переводится в ``snake_case``.

.. code-block:: python

   from vkapi import Bot

   bot = Bot("TOKEN", group_id=123456)

   message_id = await bot.messages.send(
       peer_id=2_000_000_001,
       random_id=bot.next_random_id(),
       message="Привет",
   )

Можно создать объект метода явно. Это удобно, когда метод нужно передать,
протестировать сериализацию параметров или вызвать через ``bot(method)``.

.. code-block:: python

   from vkapi import Bot
   from vkapi.methods import MessagesSend

   bot = Bot("TOKEN", group_id=123456)
   method = MessagesSend(
       peer_id=2_000_000_001,
       random_id=bot.next_random_id(),
       message="Привет",
   )

   message_id = await bot(method)

Если нужный метод отсутствует в сгенерированной схеме или нужно быстро проверить
новый метод VK, используйте raw-вызов. В этом режиме параметры не проверяются
pydantic-моделью, но проходят через тот же HTTP-клиент и rate limiter.

.. code-block:: python

   result = await bot.api(
       "messages.send",
       peer_id=2_000_000_001,
       random_id=bot.next_random_id(),
       message="Привет",
   )

Параметры
---------

* Обязательные параметры перечислены в колонке ``Обязательные параметры``.
* ``None`` не отправляется в VK API.
* ``bool`` сериализуется как ``1`` или ``0``.
* ``dict``, ``list`` и pydantic-модели сериализуются в JSON-строку. Это полезно
  для параметров вроде ``keyboard``, ``template``, ``payload`` и ``fields``.
* В именах параметров используется Python ``snake_case``. Если в VK-схеме имя
  конфликтует с синтаксисом Python, SDK использует alias pydantic-модели.

Примеры
-------

Отправить сообщение с клавиатурой:

.. code-block:: python

   from vkapi import Bot, Keyboard, KeyboardButtonColor

   bot = Bot("TOKEN", group_id=123456)

   keyboard = (
       Keyboard(inline=True)
       .add_text("Профиль", payload={"action": "profile"}, color=KeyboardButtonColor.PRIMARY)
       .row()
       .add_callback("Обновить", payload={"action": "refresh"})
   )

   await bot.messages.send(
       peer_id=2_000_000_001,
       random_id=bot.next_random_id(),
       message="Выберите действие",
       keyboard=keyboard.as_json(),
   )

Получить пользователей с полями профиля:

.. code-block:: python

   users = await bot.users.get(
       user_ids=[1, 2],
       fields=["photo_100", "screen_name"],
   )

Загрузить фото и отправить его как attachment:

.. code-block:: python

   attachment = await bot.upload.message_photo(
       peer_id=2_000_000_001,
       path="/path/to/photo.jpg",
   )

   await bot.messages.send(
       peer_id=2_000_000_001,
       random_id=bot.next_random_id(),
       attachment=attachment,
   )

Ответить на входящее сообщение из обработчика:

.. code-block:: python

   from vkapi.types import Message


   async def handler(message: Message) -> None:
       await message.reply("Ответ на сообщение")
       await message.edit("Текст изменен")

Вызвать ``execute``:

.. code-block:: python

   result = await bot.api("execute", code="return 1;")

Список методов
-------------------------

В колонке ``Вызов`` показан готовый Python-вызов. Например, строка
``bot.messages.send(...)`` вызывает VK-метод ``messages.send``.

account
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `account.ban <https://dev.vk.com/method/account.ban>`__
     - ``bot.account.ban(...)``
     - ``AccountBan``
     - нет
   * - `account.changePassword <https://dev.vk.com/method/account.changePassword>`__
     - ``bot.account.change_password(...)``
     - ``AccountChangePassword``
     - ``new_password``
   * - `account.getActiveOffers <https://dev.vk.com/method/account.getActiveOffers>`__
     - ``bot.account.get_active_offers(...)``
     - ``AccountGetActiveOffers``
     - нет
   * - `account.getAppPermissions <https://dev.vk.com/method/account.getAppPermissions>`__
     - ``bot.account.get_app_permissions(...)``
     - ``AccountGetAppPermissions``
     - нет
   * - `account.getBanned <https://dev.vk.com/method/account.getBanned>`__
     - ``bot.account.get_banned(...)``
     - ``AccountGetBanned``
     - нет
   * - `account.getCounters <https://dev.vk.com/method/account.getCounters>`__
     - ``bot.account.get_counters(...)``
     - ``AccountGetCounters``
     - нет
   * - `account.getInfo <https://dev.vk.com/method/account.getInfo>`__
     - ``bot.account.get_info(...)``
     - ``AccountGetInfo``
     - нет
   * - `account.getProfileInfo <https://dev.vk.com/method/account.getProfileInfo>`__
     - ``bot.account.get_profile_info(...)``
     - ``AccountGetProfileInfo``
     - нет
   * - `account.getPushSettings <https://dev.vk.com/method/account.getPushSettings>`__
     - ``bot.account.get_push_settings(...)``
     - ``AccountGetPushSettings``
     - нет
   * - `account.registerDevice <https://dev.vk.com/method/account.registerDevice>`__
     - ``bot.account.register_device(...)``
     - ``AccountRegisterDevice``
     - ``token``, ``device_id``
   * - `account.saveProfileInfo <https://dev.vk.com/method/account.saveProfileInfo>`__
     - ``bot.account.save_profile_info(...)``
     - ``AccountSaveProfileInfo``
     - нет
   * - `account.setInfo <https://dev.vk.com/method/account.setInfo>`__
     - ``bot.account.set_info(...)``
     - ``AccountSetInfo``
     - нет
   * - `account.setOffline <https://dev.vk.com/method/account.setOffline>`__
     - ``bot.account.set_offline(...)``
     - ``AccountSetOffline``
     - нет
   * - `account.setOnline <https://dev.vk.com/method/account.setOnline>`__
     - ``bot.account.set_online(...)``
     - ``AccountSetOnline``
     - нет
   * - `account.setPushSettings <https://dev.vk.com/method/account.setPushSettings>`__
     - ``bot.account.set_push_settings(...)``
     - ``AccountSetPushSettings``
     - ``device_id``
   * - `account.setSilenceMode <https://dev.vk.com/method/account.setSilenceMode>`__
     - ``bot.account.set_silence_mode(...)``
     - ``AccountSetSilenceMode``
     - нет
   * - `account.unban <https://dev.vk.com/method/account.unban>`__
     - ``bot.account.unban(...)``
     - ``AccountUnban``
     - нет
   * - `account.unregisterDevice <https://dev.vk.com/method/account.unregisterDevice>`__
     - ``bot.account.unregister_device(...)``
     - ``AccountUnregisterDevice``
     - нет

ads
~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `ads.addOfficeUsers <https://dev.vk.com/method/ads.addOfficeUsers>`__
     - ``bot.ads.add_office_users(...)``
     - ``AdsAddOfficeUsers``
     - ``account_id``, ``data``
   * - `ads.checkLink <https://dev.vk.com/method/ads.checkLink>`__
     - ``bot.ads.check_link(...)``
     - ``AdsCheckLink``
     - ``account_id``, ``link_type``, ``link_url``
   * - `ads.createAds <https://dev.vk.com/method/ads.createAds>`__
     - ``bot.ads.create_ads(...)``
     - ``AdsCreateAds``
     - ``account_id``, ``data``
   * - `ads.createCampaigns <https://dev.vk.com/method/ads.createCampaigns>`__
     - ``bot.ads.create_campaigns(...)``
     - ``AdsCreateCampaigns``
     - ``account_id``, ``data``
   * - `ads.createClients <https://dev.vk.com/method/ads.createClients>`__
     - ``bot.ads.create_clients(...)``
     - ``AdsCreateClients``
     - ``account_id``, ``data``
   * - `ads.createLookalikeRequest <https://dev.vk.com/method/ads.createLookalikeRequest>`__
     - ``bot.ads.create_lookalike_request(...)``
     - ``AdsCreateLookalikeRequest``
     - ``account_id``, ``source_type``
   * - `ads.createTargetGroup <https://dev.vk.com/method/ads.createTargetGroup>`__
     - ``bot.ads.create_target_group(...)``
     - ``AdsCreateTargetGroup``
     - ``account_id``, ``name``, ``lifetime``
   * - `ads.createTargetPixel <https://dev.vk.com/method/ads.createTargetPixel>`__
     - ``bot.ads.create_target_pixel(...)``
     - ``AdsCreateTargetPixel``
     - ``account_id``, ``name``, ``category_id``
   * - `ads.deleteAds <https://dev.vk.com/method/ads.deleteAds>`__
     - ``bot.ads.delete_ads(...)``
     - ``AdsDeleteAds``
     - ``account_id``, ``ids``
   * - `ads.deleteCampaigns <https://dev.vk.com/method/ads.deleteCampaigns>`__
     - ``bot.ads.delete_campaigns(...)``
     - ``AdsDeleteCampaigns``
     - ``account_id``, ``ids``
   * - `ads.deleteClients <https://dev.vk.com/method/ads.deleteClients>`__
     - ``bot.ads.delete_clients(...)``
     - ``AdsDeleteClients``
     - ``account_id``, ``ids``
   * - `ads.deleteTargetGroup <https://dev.vk.com/method/ads.deleteTargetGroup>`__
     - ``bot.ads.delete_target_group(...)``
     - ``AdsDeleteTargetGroup``
     - ``account_id``, ``target_group_id``
   * - `ads.deleteTargetPixel <https://dev.vk.com/method/ads.deleteTargetPixel>`__
     - ``bot.ads.delete_target_pixel(...)``
     - ``AdsDeleteTargetPixel``
     - ``account_id``, ``target_pixel_id``
   * - `ads.getAccounts <https://dev.vk.com/method/ads.getAccounts>`__
     - ``bot.ads.get_accounts(...)``
     - ``AdsGetAccounts``
     - нет
   * - `ads.getAds <https://dev.vk.com/method/ads.getAds>`__
     - ``bot.ads.get_ads(...)``
     - ``AdsGetAds``
     - ``account_id``
   * - `ads.getAdsLayout <https://dev.vk.com/method/ads.getAdsLayout>`__
     - ``bot.ads.get_ads_layout(...)``
     - ``AdsGetAdsLayout``
     - ``account_id``
   * - `ads.getAdsTargeting <https://dev.vk.com/method/ads.getAdsTargeting>`__
     - ``bot.ads.get_ads_targeting(...)``
     - ``AdsGetAdsTargeting``
     - ``account_id``
   * - `ads.getBudget <https://dev.vk.com/method/ads.getBudget>`__
     - ``bot.ads.get_budget(...)``
     - ``AdsGetBudget``
     - ``account_id``
   * - `ads.getCampaigns <https://dev.vk.com/method/ads.getCampaigns>`__
     - ``bot.ads.get_campaigns(...)``
     - ``AdsGetCampaigns``
     - ``account_id``
   * - `ads.getCategories <https://dev.vk.com/method/ads.getCategories>`__
     - ``bot.ads.get_categories(...)``
     - ``AdsGetCategories``
     - нет
   * - `ads.getClients <https://dev.vk.com/method/ads.getClients>`__
     - ``bot.ads.get_clients(...)``
     - ``AdsGetClients``
     - ``account_id``
   * - `ads.getDemographics <https://dev.vk.com/method/ads.getDemographics>`__
     - ``bot.ads.get_demographics(...)``
     - ``AdsGetDemographics``
     - ``account_id``, ``ids_type``, ``ids``, ``period``, ``date_from``, ``date_to``
   * - `ads.getFloodStats <https://dev.vk.com/method/ads.getFloodStats>`__
     - ``bot.ads.get_flood_stats(...)``
     - ``AdsGetFloodStats``
     - ``account_id``
   * - `ads.getLookalikeRequests <https://dev.vk.com/method/ads.getLookalikeRequests>`__
     - ``bot.ads.get_lookalike_requests(...)``
     - ``AdsGetLookalikeRequests``
     - ``account_id``
   * - `ads.getMusicians <https://dev.vk.com/method/ads.getMusicians>`__
     - ``bot.ads.get_musicians(...)``
     - ``AdsGetMusicians``
     - ``artist_name``
   * - `ads.getMusiciansByIds <https://dev.vk.com/method/ads.getMusiciansByIds>`__
     - ``bot.ads.get_musicians_by_ids(...)``
     - ``AdsGetMusiciansByIds``
     - ``ids``
   * - `ads.getOfficeUsers <https://dev.vk.com/method/ads.getOfficeUsers>`__
     - ``bot.ads.get_office_users(...)``
     - ``AdsGetOfficeUsers``
     - ``account_id``
   * - `ads.getPostsReach <https://dev.vk.com/method/ads.getPostsReach>`__
     - ``bot.ads.get_posts_reach(...)``
     - ``AdsGetPostsReach``
     - ``account_id``, ``ids_type``, ``ids``
   * - `ads.getRejectionReason <https://dev.vk.com/method/ads.getRejectionReason>`__
     - ``bot.ads.get_rejection_reason(...)``
     - ``AdsGetRejectionReason``
     - ``account_id``, ``ad_id``
   * - `ads.getStatistics <https://dev.vk.com/method/ads.getStatistics>`__
     - ``bot.ads.get_statistics(...)``
     - ``AdsGetStatistics``
     - ``account_id``, ``ids_type``, ``ids``, ``period``, ``date_from``, ``date_to``
   * - `ads.getSuggestions <https://dev.vk.com/method/ads.getSuggestions>`__
     - ``bot.ads.get_suggestions(...)``
     - ``AdsGetSuggestions``
     - ``section``
   * - `ads.getTargetGroups <https://dev.vk.com/method/ads.getTargetGroups>`__
     - ``bot.ads.get_target_groups(...)``
     - ``AdsGetTargetGroups``
     - ``account_id``
   * - `ads.getTargetingStats <https://dev.vk.com/method/ads.getTargetingStats>`__
     - ``bot.ads.get_targeting_stats(...)``
     - ``AdsGetTargetingStats``
     - ``account_id``, ``link_url``
   * - `ads.getTargetPixels <https://dev.vk.com/method/ads.getTargetPixels>`__
     - ``bot.ads.get_target_pixels(...)``
     - ``AdsGetTargetPixels``
     - ``account_id``
   * - `ads.getUploadURL <https://dev.vk.com/method/ads.getUploadURL>`__
     - ``bot.ads.get_upload_u_r_l(...)``
     - ``AdsGetUploadURL``
     - ``ad_format``
   * - `ads.getVideoUploadURL <https://dev.vk.com/method/ads.getVideoUploadURL>`__
     - ``bot.ads.get_video_upload_u_r_l(...)``
     - ``AdsGetVideoUploadURL``
     - нет
   * - `ads.importTargetContacts <https://dev.vk.com/method/ads.importTargetContacts>`__
     - ``bot.ads.import_target_contacts(...)``
     - ``AdsImportTargetContacts``
     - ``account_id``, ``target_group_id``, ``contacts``
   * - `ads.removeOfficeUsers <https://dev.vk.com/method/ads.removeOfficeUsers>`__
     - ``bot.ads.remove_office_users(...)``
     - ``AdsRemoveOfficeUsers``
     - ``account_id``, ``ids``
   * - `ads.removeTargetContacts <https://dev.vk.com/method/ads.removeTargetContacts>`__
     - ``bot.ads.remove_target_contacts(...)``
     - ``AdsRemoveTargetContacts``
     - ``account_id``, ``target_group_id``, ``contacts``
   * - `ads.saveLookalikeRequestResult <https://dev.vk.com/method/ads.saveLookalikeRequestResult>`__
     - ``bot.ads.save_lookalike_request_result(...)``
     - ``AdsSaveLookalikeRequestResult``
     - ``account_id``, ``request_id``, ``level``
   * - `ads.shareTargetGroup <https://dev.vk.com/method/ads.shareTargetGroup>`__
     - ``bot.ads.share_target_group(...)``
     - ``AdsShareTargetGroup``
     - ``account_id``, ``target_group_id``
   * - `ads.updateAds <https://dev.vk.com/method/ads.updateAds>`__
     - ``bot.ads.update_ads(...)``
     - ``AdsUpdateAds``
     - ``account_id``, ``data``
   * - `ads.updateCampaigns <https://dev.vk.com/method/ads.updateCampaigns>`__
     - ``bot.ads.update_campaigns(...)``
     - ``AdsUpdateCampaigns``
     - ``account_id``, ``data``
   * - `ads.updateClients <https://dev.vk.com/method/ads.updateClients>`__
     - ``bot.ads.update_clients(...)``
     - ``AdsUpdateClients``
     - ``account_id``, ``data``
   * - `ads.updateOfficeUsers <https://dev.vk.com/method/ads.updateOfficeUsers>`__
     - ``bot.ads.update_office_users(...)``
     - ``AdsUpdateOfficeUsers``
     - ``account_id``, ``data``
   * - `ads.updateTargetGroup <https://dev.vk.com/method/ads.updateTargetGroup>`__
     - ``bot.ads.update_target_group(...)``
     - ``AdsUpdateTargetGroup``
     - ``account_id``, ``target_group_id``, ``name``, ``lifetime``
   * - `ads.updateTargetPixel <https://dev.vk.com/method/ads.updateTargetPixel>`__
     - ``bot.ads.update_target_pixel(...)``
     - ``AdsUpdateTargetPixel``
     - ``account_id``, ``target_pixel_id``, ``name``, ``category_id``

api
~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `execute <https://dev.vk.com/method/execute>`__
     - ``bot.api("execute", ...)``
     - ``Execute``
     - нет

appWidgets
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `appWidgets.getAppImages <https://dev.vk.com/method/appWidgets.getAppImages>`__
     - ``bot.appWidgets.get_app_images(...)``
     - ``AppWidgetsGetAppImages``
     - нет
   * - `appWidgets.getAppImageUploadServer <https://dev.vk.com/method/appWidgets.getAppImageUploadServer>`__
     - ``bot.appWidgets.get_app_image_upload_server(...)``
     - ``AppWidgetsGetAppImageUploadServer``
     - ``image_type``
   * - `appWidgets.getGroupImages <https://dev.vk.com/method/appWidgets.getGroupImages>`__
     - ``bot.appWidgets.get_group_images(...)``
     - ``AppWidgetsGetGroupImages``
     - нет
   * - `appWidgets.getGroupImageUploadServer <https://dev.vk.com/method/appWidgets.getGroupImageUploadServer>`__
     - ``bot.appWidgets.get_group_image_upload_server(...)``
     - ``AppWidgetsGetGroupImageUploadServer``
     - ``image_type``
   * - `appWidgets.getImagesById <https://dev.vk.com/method/appWidgets.getImagesById>`__
     - ``bot.appWidgets.get_images_by_id(...)``
     - ``AppWidgetsGetImagesById``
     - ``images``
   * - `appWidgets.saveAppImage <https://dev.vk.com/method/appWidgets.saveAppImage>`__
     - ``bot.appWidgets.save_app_image(...)``
     - ``AppWidgetsSaveAppImage``
     - ``hash``, ``image``
   * - `appWidgets.saveGroupImage <https://dev.vk.com/method/appWidgets.saveGroupImage>`__
     - ``bot.appWidgets.save_group_image(...)``
     - ``AppWidgetsSaveGroupImage``
     - ``hash``, ``image``
   * - `appWidgets.update <https://dev.vk.com/method/appWidgets.update>`__
     - ``bot.appWidgets.update(...)``
     - ``AppWidgetsUpdate``
     - ``code``, ``type``

apps
~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `apps.addSnippet <https://dev.vk.com/method/apps.addSnippet>`__
     - ``bot.apps.add_snippet(...)``
     - ``AppsAddSnippet``
     - нет
   * - `apps.addUsersToTestingGroup <https://dev.vk.com/method/apps.addUsersToTestingGroup>`__
     - ``bot.apps.add_users_to_testing_group(...)``
     - ``AppsAddUsersToTestingGroup``
     - ``user_ids``, ``group_id``
   * - `apps.deleteAppRequests <https://dev.vk.com/method/apps.deleteAppRequests>`__
     - ``bot.apps.delete_app_requests(...)``
     - ``AppsDeleteAppRequests``
     - нет
   * - `apps.deleteSnippet <https://dev.vk.com/method/apps.deleteSnippet>`__
     - ``bot.apps.delete_snippet(...)``
     - ``AppsDeleteSnippet``
     - нет
   * - `apps.get <https://dev.vk.com/method/apps.get>`__
     - ``bot.apps.get(...)``
     - ``AppsGet``
     - нет
   * - `apps.getCatalog <https://dev.vk.com/method/apps.getCatalog>`__
     - ``bot.apps.get_catalog(...)``
     - ``AppsGetCatalog``
     - нет
   * - `apps.getFriendsList <https://dev.vk.com/method/apps.getFriendsList>`__
     - ``bot.apps.get_friends_list(...)``
     - ``AppsGetFriendsList``
     - нет
   * - `apps.getLeaderboard <https://dev.vk.com/method/apps.getLeaderboard>`__
     - ``bot.apps.get_leaderboard(...)``
     - ``AppsGetLeaderboard``
     - ``type``
   * - `apps.getMiniAppPolicies <https://dev.vk.com/method/apps.getMiniAppPolicies>`__
     - ``bot.apps.get_mini_app_policies(...)``
     - ``AppsGetMiniAppPolicies``
     - ``app_id``
   * - `apps.getScopes <https://dev.vk.com/method/apps.getScopes>`__
     - ``bot.apps.get_scopes(...)``
     - ``AppsGetScopes``
     - нет
   * - `apps.getScore <https://dev.vk.com/method/apps.getScore>`__
     - ``bot.apps.get_score(...)``
     - ``AppsGetScore``
     - нет
   * - `apps.getSnippets <https://dev.vk.com/method/apps.getSnippets>`__
     - ``bot.apps.get_snippets(...)``
     - ``AppsGetSnippets``
     - нет
   * - `apps.getTestingGroups <https://dev.vk.com/method/apps.getTestingGroups>`__
     - ``bot.apps.get_testing_groups(...)``
     - ``AppsGetTestingGroups``
     - нет
   * - `apps.isNotificationsAllowed <https://dev.vk.com/method/apps.isNotificationsAllowed>`__
     - ``bot.apps.is_notifications_allowed(...)``
     - ``AppsIsNotificationsAllowed``
     - нет
   * - `apps.promoHasActiveGift <https://dev.vk.com/method/apps.promoHasActiveGift>`__
     - ``bot.apps.promo_has_active_gift(...)``
     - ``AppsPromoHasActiveGift``
     - ``promo_id``
   * - `apps.promoUseGift <https://dev.vk.com/method/apps.promoUseGift>`__
     - ``bot.apps.promo_use_gift(...)``
     - ``AppsPromoUseGift``
     - ``promo_id``
   * - `apps.removeTestingGroup <https://dev.vk.com/method/apps.removeTestingGroup>`__
     - ``bot.apps.remove_testing_group(...)``
     - ``AppsRemoveTestingGroup``
     - ``group_id``
   * - `apps.removeUsersFromTestingGroups <https://dev.vk.com/method/apps.removeUsersFromTestingGroups>`__
     - ``bot.apps.remove_users_from_testing_groups(...)``
     - ``AppsRemoveUsersFromTestingGroups``
     - ``user_ids``
   * - `apps.sendRequest <https://dev.vk.com/method/apps.sendRequest>`__
     - ``bot.apps.send_request(...)``
     - ``AppsSendRequest``
     - ``user_id``
   * - `apps.updateMetaForTestingGroup <https://dev.vk.com/method/apps.updateMetaForTestingGroup>`__
     - ``bot.apps.update_meta_for_testing_group(...)``
     - ``AppsUpdateMetaForTestingGroup``
     - ``webview``, ``name``, ``platforms``

auth
~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `auth.restore <https://dev.vk.com/method/auth.restore>`__
     - ``bot.auth.restore(...)``
     - ``AuthRestore``
     - ``phone``, ``last_name``

board
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `board.addTopic <https://dev.vk.com/method/board.addTopic>`__
     - ``bot.board.add_topic(...)``
     - ``BoardAddTopic``
     - ``group_id``, ``title``
   * - `board.closeTopic <https://dev.vk.com/method/board.closeTopic>`__
     - ``bot.board.close_topic(...)``
     - ``BoardCloseTopic``
     - ``group_id``, ``topic_id``
   * - `board.createComment <https://dev.vk.com/method/board.createComment>`__
     - ``bot.board.create_comment(...)``
     - ``BoardCreateComment``
     - ``group_id``, ``topic_id``
   * - `board.deleteComment <https://dev.vk.com/method/board.deleteComment>`__
     - ``bot.board.delete_comment(...)``
     - ``BoardDeleteComment``
     - ``group_id``, ``topic_id``, ``comment_id``
   * - `board.deleteTopic <https://dev.vk.com/method/board.deleteTopic>`__
     - ``bot.board.delete_topic(...)``
     - ``BoardDeleteTopic``
     - ``group_id``, ``topic_id``
   * - `board.editComment <https://dev.vk.com/method/board.editComment>`__
     - ``bot.board.edit_comment(...)``
     - ``BoardEditComment``
     - ``group_id``, ``topic_id``, ``comment_id``
   * - `board.editTopic <https://dev.vk.com/method/board.editTopic>`__
     - ``bot.board.edit_topic(...)``
     - ``BoardEditTopic``
     - ``group_id``, ``topic_id``, ``title``
   * - `board.fixTopic <https://dev.vk.com/method/board.fixTopic>`__
     - ``bot.board.fix_topic(...)``
     - ``BoardFixTopic``
     - ``group_id``, ``topic_id``
   * - `board.getComments <https://dev.vk.com/method/board.getComments>`__
     - ``bot.board.get_comments(...)``
     - ``BoardGetComments``
     - ``group_id``, ``topic_id``
   * - `board.getTopics <https://dev.vk.com/method/board.getTopics>`__
     - ``bot.board.get_topics(...)``
     - ``BoardGetTopics``
     - ``group_id``
   * - `board.openTopic <https://dev.vk.com/method/board.openTopic>`__
     - ``bot.board.open_topic(...)``
     - ``BoardOpenTopic``
     - ``group_id``, ``topic_id``
   * - `board.restoreComment <https://dev.vk.com/method/board.restoreComment>`__
     - ``bot.board.restore_comment(...)``
     - ``BoardRestoreComment``
     - ``group_id``, ``topic_id``, ``comment_id``
   * - `board.unfixTopic <https://dev.vk.com/method/board.unfixTopic>`__
     - ``bot.board.unfix_topic(...)``
     - ``BoardUnfixTopic``
     - ``group_id``, ``topic_id``

bugtracker
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `bugtracker.addCompanyGroupsMembers <https://dev.vk.com/method/bugtracker.addCompanyGroupsMembers>`__
     - ``bot.bugtracker.add_company_groups_members(...)``
     - ``BugtrackerAddCompanyGroupsMembers``
     - ``company_id``, ``user_ids``, ``company_group_ids``
   * - `bugtracker.addCompanyMembers <https://dev.vk.com/method/bugtracker.addCompanyMembers>`__
     - ``bot.bugtracker.add_company_members(...)``
     - ``BugtrackerAddCompanyMembers``
     - ``user_ids``, ``company_id``
   * - `bugtracker.changeBugreportStatus <https://dev.vk.com/method/bugtracker.changeBugreportStatus>`__
     - ``bot.bugtracker.change_bugreport_status(...)``
     - ``BugtrackerChangeBugreportStatus``
     - ``bugreport_id``
   * - `bugtracker.createComment <https://dev.vk.com/method/bugtracker.createComment>`__
     - ``bot.bugtracker.create_comment(...)``
     - ``BugtrackerCreateComment``
     - ``bugreport_id``
   * - `bugtracker.getBugreportById <https://dev.vk.com/method/bugtracker.getBugreportById>`__
     - ``bot.bugtracker.get_bugreport_by_id(...)``
     - ``BugtrackerGetBugreportById``
     - ``bugreport_id``
   * - `bugtracker.getCompanyGroupMembers <https://dev.vk.com/method/bugtracker.getCompanyGroupMembers>`__
     - ``bot.bugtracker.get_company_group_members(...)``
     - ``BugtrackerGetCompanyGroupMembers``
     - ``company_id``, ``company_group_id``
   * - `bugtracker.getCompanyMembers <https://dev.vk.com/method/bugtracker.getCompanyMembers>`__
     - ``bot.bugtracker.get_company_members(...)``
     - ``BugtrackerGetCompanyMembers``
     - ``company_id``
   * - `bugtracker.getDownloadVersionUrl <https://dev.vk.com/method/bugtracker.getDownloadVersionUrl>`__
     - ``bot.bugtracker.get_download_version_url(...)``
     - ``BugtrackerGetDownloadVersionUrl``
     - ``product_id``, ``version_id``
   * - `bugtracker.getProductBuildUploadServer <https://dev.vk.com/method/bugtracker.getProductBuildUploadServer>`__
     - ``bot.bugtracker.get_product_build_upload_server(...)``
     - ``BugtrackerGetProductBuildUploadServer``
     - ``product_id``
   * - `bugtracker.removeCompanyGroupMember <https://dev.vk.com/method/bugtracker.removeCompanyGroupMember>`__
     - ``bot.bugtracker.remove_company_group_member(...)``
     - ``BugtrackerRemoveCompanyGroupMember``
     - ``company_id``, ``user_id``, ``company_group_id``
   * - `bugtracker.removeCompanyMember <https://dev.vk.com/method/bugtracker.removeCompanyMember>`__
     - ``bot.bugtracker.remove_company_member(...)``
     - ``BugtrackerRemoveCompanyMember``
     - ``user_id``, ``company_id``
   * - `bugtracker.saveProductVersion <https://dev.vk.com/method/bugtracker.saveProductVersion>`__
     - ``bot.bugtracker.save_product_version(...)``
     - ``BugtrackerSaveProductVersion``
     - ``title``
   * - `bugtracker.setCompanyMemberRole <https://dev.vk.com/method/bugtracker.setCompanyMemberRole>`__
     - ``bot.bugtracker.set_company_member_role(...)``
     - ``BugtrackerSetCompanyMemberRole``
     - ``user_id``, ``company_id``, ``role``
   * - `bugtracker.setProductIsOver <https://dev.vk.com/method/bugtracker.setProductIsOver>`__
     - ``bot.bugtracker.set_product_is_over(...)``
     - ``BugtrackerSetProductIsOver``
     - ``product_id``

calls
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `calls.forceFinish <https://dev.vk.com/method/calls.forceFinish>`__
     - ``bot.calls.force_finish(...)``
     - ``CallsForceFinish``
     - ``call_id``
   * - `calls.start <https://dev.vk.com/method/calls.start>`__
     - ``bot.calls.start(...)``
     - ``CallsStart``
     - нет

database
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `database.getChairs <https://dev.vk.com/method/database.getChairs>`__
     - ``bot.database.get_chairs(...)``
     - ``DatabaseGetChairs``
     - ``faculty_id``
   * - `database.getCities <https://dev.vk.com/method/database.getCities>`__
     - ``bot.database.get_cities(...)``
     - ``DatabaseGetCities``
     - нет
   * - `database.getCitiesById <https://dev.vk.com/method/database.getCitiesById>`__
     - ``bot.database.get_cities_by_id(...)``
     - ``DatabaseGetCitiesById``
     - нет
   * - `database.getCountries <https://dev.vk.com/method/database.getCountries>`__
     - ``bot.database.get_countries(...)``
     - ``DatabaseGetCountries``
     - нет
   * - `database.getCountriesById <https://dev.vk.com/method/database.getCountriesById>`__
     - ``bot.database.get_countries_by_id(...)``
     - ``DatabaseGetCountriesById``
     - нет
   * - `database.getFaculties <https://dev.vk.com/method/database.getFaculties>`__
     - ``bot.database.get_faculties(...)``
     - ``DatabaseGetFaculties``
     - ``university_id``
   * - `database.getMetroStations <https://dev.vk.com/method/database.getMetroStations>`__
     - ``bot.database.get_metro_stations(...)``
     - ``DatabaseGetMetroStations``
     - ``city_id``
   * - `database.getMetroStationsById <https://dev.vk.com/method/database.getMetroStationsById>`__
     - ``bot.database.get_metro_stations_by_id(...)``
     - ``DatabaseGetMetroStationsById``
     - нет
   * - `database.getRegions <https://dev.vk.com/method/database.getRegions>`__
     - ``bot.database.get_regions(...)``
     - ``DatabaseGetRegions``
     - нет
   * - `database.getSchoolClasses <https://dev.vk.com/method/database.getSchoolClasses>`__
     - ``bot.database.get_school_classes(...)``
     - ``DatabaseGetSchoolClasses``
     - нет
   * - `database.getSchools <https://dev.vk.com/method/database.getSchools>`__
     - ``bot.database.get_schools(...)``
     - ``DatabaseGetSchools``
     - ``city_id``
   * - `database.getUniversities <https://dev.vk.com/method/database.getUniversities>`__
     - ``bot.database.get_universities(...)``
     - ``DatabaseGetUniversities``
     - нет

docs
~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `docs.add <https://dev.vk.com/method/docs.add>`__
     - ``bot.docs.add(...)``
     - ``DocsAdd``
     - ``owner_id``, ``doc_id``
   * - `docs.delete <https://dev.vk.com/method/docs.delete>`__
     - ``bot.docs.delete(...)``
     - ``DocsDelete``
     - ``owner_id``, ``doc_id``
   * - `docs.edit <https://dev.vk.com/method/docs.edit>`__
     - ``bot.docs.edit(...)``
     - ``DocsEdit``
     - ``doc_id``, ``title``
   * - `docs.get <https://dev.vk.com/method/docs.get>`__
     - ``bot.docs.get(...)``
     - ``DocsGet``
     - нет
   * - `docs.getById <https://dev.vk.com/method/docs.getById>`__
     - ``bot.docs.get_by_id(...)``
     - ``DocsGetById``
     - ``docs``
   * - `docs.getMessagesUploadServer <https://dev.vk.com/method/docs.getMessagesUploadServer>`__
     - ``bot.docs.get_messages_upload_server(...)``
     - ``DocsGetMessagesUploadServer``
     - нет
   * - `docs.getTypes <https://dev.vk.com/method/docs.getTypes>`__
     - ``bot.docs.get_types(...)``
     - ``DocsGetTypes``
     - нет
   * - `docs.getUploadServer <https://dev.vk.com/method/docs.getUploadServer>`__
     - ``bot.docs.get_upload_server(...)``
     - ``DocsGetUploadServer``
     - нет
   * - `docs.getWallUploadServer <https://dev.vk.com/method/docs.getWallUploadServer>`__
     - ``bot.docs.get_wall_upload_server(...)``
     - ``DocsGetWallUploadServer``
     - нет
   * - `docs.restore <https://dev.vk.com/method/docs.restore>`__
     - ``bot.docs.restore(...)``
     - ``DocsRestore``
     - ``owner_id``, ``doc_id``
   * - `docs.save <https://dev.vk.com/method/docs.save>`__
     - ``bot.docs.save(...)``
     - ``DocsSave``
     - ``file``
   * - `docs.search <https://dev.vk.com/method/docs.search>`__
     - ``bot.docs.search(...)``
     - ``DocsSearch``
     - нет

donut
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `donut.getFriends <https://dev.vk.com/method/donut.getFriends>`__
     - ``bot.donut.get_friends(...)``
     - ``DonutGetFriends``
     - ``owner_id``
   * - `donut.getSubscription <https://dev.vk.com/method/donut.getSubscription>`__
     - ``bot.donut.get_subscription(...)``
     - ``DonutGetSubscription``
     - ``owner_id``
   * - `donut.getSubscriptions <https://dev.vk.com/method/donut.getSubscriptions>`__
     - ``bot.donut.get_subscriptions(...)``
     - ``DonutGetSubscriptions``
     - нет
   * - `donut.isDon <https://dev.vk.com/method/donut.isDon>`__
     - ``bot.donut.is_don(...)``
     - ``DonutIsDon``
     - ``owner_id``

downloadedGames
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `downloadedGames.getPaidStatus <https://dev.vk.com/method/downloadedGames.getPaidStatus>`__
     - ``bot.downloadedGames.get_paid_status(...)``
     - ``DownloadedGamesGetPaidStatus``
     - нет

fave
~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `fave.addArticle <https://dev.vk.com/method/fave.addArticle>`__
     - ``bot.fave.add_article(...)``
     - ``FaveAddArticle``
     - ``url``
   * - `fave.addLink <https://dev.vk.com/method/fave.addLink>`__
     - ``bot.fave.add_link(...)``
     - ``FaveAddLink``
     - ``link``
   * - `fave.addPage <https://dev.vk.com/method/fave.addPage>`__
     - ``bot.fave.add_page(...)``
     - ``FaveAddPage``
     - нет
   * - `fave.addPost <https://dev.vk.com/method/fave.addPost>`__
     - ``bot.fave.add_post(...)``
     - ``FaveAddPost``
     - ``owner_id``, ``id``
   * - `fave.addProduct <https://dev.vk.com/method/fave.addProduct>`__
     - ``bot.fave.add_product(...)``
     - ``FaveAddProduct``
     - ``owner_id``, ``id``
   * - `fave.addTag <https://dev.vk.com/method/fave.addTag>`__
     - ``bot.fave.add_tag(...)``
     - ``FaveAddTag``
     - нет
   * - `fave.addVideo <https://dev.vk.com/method/fave.addVideo>`__
     - ``bot.fave.add_video(...)``
     - ``FaveAddVideo``
     - ``owner_id``, ``id``
   * - `fave.editTag <https://dev.vk.com/method/fave.editTag>`__
     - ``bot.fave.edit_tag(...)``
     - ``FaveEditTag``
     - ``id``, ``name``
   * - `fave.get <https://dev.vk.com/method/fave.get>`__
     - ``bot.fave.get(...)``
     - ``FaveGet``
     - нет
   * - `fave.getPages <https://dev.vk.com/method/fave.getPages>`__
     - ``bot.fave.get_pages(...)``
     - ``FaveGetPages``
     - нет
   * - `fave.getTags <https://dev.vk.com/method/fave.getTags>`__
     - ``bot.fave.get_tags(...)``
     - ``FaveGetTags``
     - нет
   * - `fave.markSeen <https://dev.vk.com/method/fave.markSeen>`__
     - ``bot.fave.mark_seen(...)``
     - ``FaveMarkSeen``
     - нет
   * - `fave.removeArticle <https://dev.vk.com/method/fave.removeArticle>`__
     - ``bot.fave.remove_article(...)``
     - ``FaveRemoveArticle``
     - ``owner_id``, ``article_id``
   * - `fave.removeLink <https://dev.vk.com/method/fave.removeLink>`__
     - ``bot.fave.remove_link(...)``
     - ``FaveRemoveLink``
     - нет
   * - `fave.removePage <https://dev.vk.com/method/fave.removePage>`__
     - ``bot.fave.remove_page(...)``
     - ``FaveRemovePage``
     - нет
   * - `fave.removePost <https://dev.vk.com/method/fave.removePost>`__
     - ``bot.fave.remove_post(...)``
     - ``FaveRemovePost``
     - ``owner_id``, ``id``
   * - `fave.removeProduct <https://dev.vk.com/method/fave.removeProduct>`__
     - ``bot.fave.remove_product(...)``
     - ``FaveRemoveProduct``
     - ``owner_id``, ``id``
   * - `fave.removeTag <https://dev.vk.com/method/fave.removeTag>`__
     - ``bot.fave.remove_tag(...)``
     - ``FaveRemoveTag``
     - ``id``
   * - `fave.removeVideo <https://dev.vk.com/method/fave.removeVideo>`__
     - ``bot.fave.remove_video(...)``
     - ``FaveRemoveVideo``
     - ``owner_id``, ``id``
   * - `fave.reorderTags <https://dev.vk.com/method/fave.reorderTags>`__
     - ``bot.fave.reorder_tags(...)``
     - ``FaveReorderTags``
     - ``ids``
   * - `fave.setPageTags <https://dev.vk.com/method/fave.setPageTags>`__
     - ``bot.fave.set_page_tags(...)``
     - ``FaveSetPageTags``
     - нет
   * - `fave.setTags <https://dev.vk.com/method/fave.setTags>`__
     - ``bot.fave.set_tags(...)``
     - ``FaveSetTags``
     - нет
   * - `fave.trackPageInteraction <https://dev.vk.com/method/fave.trackPageInteraction>`__
     - ``bot.fave.track_page_interaction(...)``
     - ``FaveTrackPageInteraction``
     - нет

friends
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `friends.add <https://dev.vk.com/method/friends.add>`__
     - ``bot.friends.add(...)``
     - ``FriendsAdd``
     - нет
   * - `friends.addList <https://dev.vk.com/method/friends.addList>`__
     - ``bot.friends.add_list(...)``
     - ``FriendsAddList``
     - ``name``
   * - `friends.areFriends <https://dev.vk.com/method/friends.areFriends>`__
     - ``bot.friends.are_friends(...)``
     - ``FriendsAreFriends``
     - ``user_ids``
   * - `friends.delete <https://dev.vk.com/method/friends.delete>`__
     - ``bot.friends.delete(...)``
     - ``FriendsDelete``
     - нет
   * - `friends.deleteAllRequests <https://dev.vk.com/method/friends.deleteAllRequests>`__
     - ``bot.friends.delete_all_requests(...)``
     - ``FriendsDeleteAllRequests``
     - нет
   * - `friends.deleteList <https://dev.vk.com/method/friends.deleteList>`__
     - ``bot.friends.delete_list(...)``
     - ``FriendsDeleteList``
     - ``list_id``
   * - `friends.edit <https://dev.vk.com/method/friends.edit>`__
     - ``bot.friends.edit(...)``
     - ``FriendsEdit``
     - ``user_id``
   * - `friends.editList <https://dev.vk.com/method/friends.editList>`__
     - ``bot.friends.edit_list(...)``
     - ``FriendsEditList``
     - ``list_id``
   * - `friends.get <https://dev.vk.com/method/friends.get>`__
     - ``bot.friends.get(...)``
     - ``FriendsGet``
     - нет
   * - `friends.getAppUsers <https://dev.vk.com/method/friends.getAppUsers>`__
     - ``bot.friends.get_app_users(...)``
     - ``FriendsGetAppUsers``
     - нет
   * - `friends.getLists <https://dev.vk.com/method/friends.getLists>`__
     - ``bot.friends.get_lists(...)``
     - ``FriendsGetLists``
     - нет
   * - `friends.getMutual <https://dev.vk.com/method/friends.getMutual>`__
     - ``bot.friends.get_mutual(...)``
     - ``FriendsGetMutual``
     - нет
   * - `friends.getOnline <https://dev.vk.com/method/friends.getOnline>`__
     - ``bot.friends.get_online(...)``
     - ``FriendsGetOnline``
     - нет
   * - `friends.getRecent <https://dev.vk.com/method/friends.getRecent>`__
     - ``bot.friends.get_recent(...)``
     - ``FriendsGetRecent``
     - нет
   * - `friends.getRequests <https://dev.vk.com/method/friends.getRequests>`__
     - ``bot.friends.get_requests(...)``
     - ``FriendsGetRequests``
     - нет
   * - `friends.getSuggestions <https://dev.vk.com/method/friends.getSuggestions>`__
     - ``bot.friends.get_suggestions(...)``
     - ``FriendsGetSuggestions``
     - нет
   * - `friends.search <https://dev.vk.com/method/friends.search>`__
     - ``bot.friends.search(...)``
     - ``FriendsSearch``
     - нет

gifts
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `gifts.get <https://dev.vk.com/method/gifts.get>`__
     - ``bot.gifts.get(...)``
     - ``GiftsGet``
     - нет

groups
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `groups.addAddress <https://dev.vk.com/method/groups.addAddress>`__
     - ``bot.groups.add_address(...)``
     - ``GroupsAddAddress``
     - ``group_id``, ``title``, ``address``, ``city_id``, ``latitude``, ``longitude``
   * - `groups.addCallbackServer <https://dev.vk.com/method/groups.addCallbackServer>`__
     - ``bot.groups.add_callback_server(...)``
     - ``GroupsAddCallbackServer``
     - ``group_id``, ``url``, ``title``
   * - `groups.addLink <https://dev.vk.com/method/groups.addLink>`__
     - ``bot.groups.add_link(...)``
     - ``GroupsAddLink``
     - ``group_id``, ``link``
   * - `groups.approveRequest <https://dev.vk.com/method/groups.approveRequest>`__
     - ``bot.groups.approve_request(...)``
     - ``GroupsApproveRequest``
     - ``group_id``, ``user_id``
   * - `groups.ban <https://dev.vk.com/method/groups.ban>`__
     - ``bot.groups.ban(...)``
     - ``GroupsBan``
     - ``group_id``
   * - `groups.create <https://dev.vk.com/method/groups.create>`__
     - ``bot.groups.create(...)``
     - ``GroupsCreate``
     - ``title``
   * - `groups.deleteAddress <https://dev.vk.com/method/groups.deleteAddress>`__
     - ``bot.groups.delete_address(...)``
     - ``GroupsDeleteAddress``
     - ``group_id``, ``address_id``
   * - `groups.deleteCallbackServer <https://dev.vk.com/method/groups.deleteCallbackServer>`__
     - ``bot.groups.delete_callback_server(...)``
     - ``GroupsDeleteCallbackServer``
     - ``group_id``, ``server_id``
   * - `groups.deleteLink <https://dev.vk.com/method/groups.deleteLink>`__
     - ``bot.groups.delete_link(...)``
     - ``GroupsDeleteLink``
     - ``group_id``, ``link_id``
   * - `groups.disableOnline <https://dev.vk.com/method/groups.disableOnline>`__
     - ``bot.groups.disable_online(...)``
     - ``GroupsDisableOnline``
     - ``group_id``
   * - `groups.edit <https://dev.vk.com/method/groups.edit>`__
     - ``bot.groups.edit(...)``
     - ``GroupsEdit``
     - ``group_id``
   * - `groups.editAddress <https://dev.vk.com/method/groups.editAddress>`__
     - ``bot.groups.edit_address(...)``
     - ``GroupsEditAddress``
     - ``group_id``, ``address_id``
   * - `groups.editCallbackServer <https://dev.vk.com/method/groups.editCallbackServer>`__
     - ``bot.groups.edit_callback_server(...)``
     - ``GroupsEditCallbackServer``
     - ``group_id``, ``server_id``, ``url``, ``title``
   * - `groups.editLink <https://dev.vk.com/method/groups.editLink>`__
     - ``bot.groups.edit_link(...)``
     - ``GroupsEditLink``
     - ``group_id``, ``link_id``
   * - `groups.editManager <https://dev.vk.com/method/groups.editManager>`__
     - ``bot.groups.edit_manager(...)``
     - ``GroupsEditManager``
     - ``group_id``, ``user_id``
   * - `groups.enableOnline <https://dev.vk.com/method/groups.enableOnline>`__
     - ``bot.groups.enable_online(...)``
     - ``GroupsEnableOnline``
     - ``group_id``
   * - `groups.get <https://dev.vk.com/method/groups.get>`__
     - ``bot.groups.get(...)``
     - ``GroupsGet``
     - нет
   * - `groups.getAddresses <https://dev.vk.com/method/groups.getAddresses>`__
     - ``bot.groups.get_addresses(...)``
     - ``GroupsGetAddresses``
     - ``group_id``
   * - `groups.getBanned <https://dev.vk.com/method/groups.getBanned>`__
     - ``bot.groups.get_banned(...)``
     - ``GroupsGetBanned``
     - ``group_id``
   * - `groups.getById <https://dev.vk.com/method/groups.getById>`__
     - ``bot.groups.get_by_id(...)``
     - ``GroupsGetById``
     - нет
   * - `groups.getCallbackConfirmationCode <https://dev.vk.com/method/groups.getCallbackConfirmationCode>`__
     - ``bot.groups.get_callback_confirmation_code(...)``
     - ``GroupsGetCallbackConfirmationCode``
     - ``group_id``
   * - `groups.getCallbackServers <https://dev.vk.com/method/groups.getCallbackServers>`__
     - ``bot.groups.get_callback_servers(...)``
     - ``GroupsGetCallbackServers``
     - ``group_id``
   * - `groups.getCallbackSettings <https://dev.vk.com/method/groups.getCallbackSettings>`__
     - ``bot.groups.get_callback_settings(...)``
     - ``GroupsGetCallbackSettings``
     - ``group_id``
   * - `groups.getCatalogInfo <https://dev.vk.com/method/groups.getCatalogInfo>`__
     - ``bot.groups.get_catalog_info(...)``
     - ``GroupsGetCatalogInfo``
     - нет
   * - `groups.getInvitedUsers <https://dev.vk.com/method/groups.getInvitedUsers>`__
     - ``bot.groups.get_invited_users(...)``
     - ``GroupsGetInvitedUsers``
     - ``group_id``
   * - `groups.getInvites <https://dev.vk.com/method/groups.getInvites>`__
     - ``bot.groups.get_invites(...)``
     - ``GroupsGetInvites``
     - нет
   * - `groups.getLongPollServer <https://dev.vk.com/method/groups.getLongPollServer>`__
     - ``bot.groups.get_long_poll_server(...)``
     - ``GroupsGetLongPollServer``
     - ``group_id``
   * - `groups.getLongPollSettings <https://dev.vk.com/method/groups.getLongPollSettings>`__
     - ``bot.groups.get_long_poll_settings(...)``
     - ``GroupsGetLongPollSettings``
     - ``group_id``
   * - `groups.getMembers <https://dev.vk.com/method/groups.getMembers>`__
     - ``bot.groups.get_members(...)``
     - ``GroupsGetMembers``
     - нет
   * - `groups.getOnlineStatus <https://dev.vk.com/method/groups.getOnlineStatus>`__
     - ``bot.groups.get_online_status(...)``
     - ``GroupsGetOnlineStatus``
     - ``group_id``
   * - `groups.getRequests <https://dev.vk.com/method/groups.getRequests>`__
     - ``bot.groups.get_requests(...)``
     - ``GroupsGetRequests``
     - ``group_id``
   * - `groups.getSettings <https://dev.vk.com/method/groups.getSettings>`__
     - ``bot.groups.get_settings(...)``
     - ``GroupsGetSettings``
     - ``group_id``
   * - `groups.getTagList <https://dev.vk.com/method/groups.getTagList>`__
     - ``bot.groups.get_tag_list(...)``
     - ``GroupsGetTagList``
     - ``group_id``
   * - `groups.getTokenPermissions <https://dev.vk.com/method/groups.getTokenPermissions>`__
     - ``bot.groups.get_token_permissions(...)``
     - ``GroupsGetTokenPermissions``
     - нет
   * - `groups.invite <https://dev.vk.com/method/groups.invite>`__
     - ``bot.groups.invite(...)``
     - ``GroupsInvite``
     - ``group_id``
   * - `groups.isMember <https://dev.vk.com/method/groups.isMember>`__
     - ``bot.groups.is_member(...)``
     - ``GroupsIsMember``
     - ``group_id``
   * - `groups.join <https://dev.vk.com/method/groups.join>`__
     - ``bot.groups.join(...)``
     - ``GroupsJoin``
     - ``group_id``
   * - `groups.leave <https://dev.vk.com/method/groups.leave>`__
     - ``bot.groups.leave(...)``
     - ``GroupsLeave``
     - ``group_id``
   * - `groups.removeUser <https://dev.vk.com/method/groups.removeUser>`__
     - ``bot.groups.remove_user(...)``
     - ``GroupsRemoveUser``
     - ``group_id``, ``user_id``
   * - `groups.reorderLink <https://dev.vk.com/method/groups.reorderLink>`__
     - ``bot.groups.reorder_link(...)``
     - ``GroupsReorderLink``
     - ``group_id``, ``link_id``
   * - `groups.search <https://dev.vk.com/method/groups.search>`__
     - ``bot.groups.search(...)``
     - ``GroupsSearch``
     - ``q``
   * - `groups.setCallbackSettings <https://dev.vk.com/method/groups.setCallbackSettings>`__
     - ``bot.groups.set_callback_settings(...)``
     - ``GroupsSetCallbackSettings``
     - ``group_id``
   * - `groups.setLongPollSettings <https://dev.vk.com/method/groups.setLongPollSettings>`__
     - ``bot.groups.set_long_poll_settings(...)``
     - ``GroupsSetLongPollSettings``
     - ``group_id``
   * - `groups.setSettings <https://dev.vk.com/method/groups.setSettings>`__
     - ``bot.groups.set_settings(...)``
     - ``GroupsSetSettings``
     - ``group_id``
   * - `groups.setUserNote <https://dev.vk.com/method/groups.setUserNote>`__
     - ``bot.groups.set_user_note(...)``
     - ``GroupsSetUserNote``
     - ``group_id``, ``user_id``
   * - `groups.tagAdd <https://dev.vk.com/method/groups.tagAdd>`__
     - ``bot.groups.tag_add(...)``
     - ``GroupsTagAdd``
     - ``group_id``, ``tag_name``
   * - `groups.tagBind <https://dev.vk.com/method/groups.tagBind>`__
     - ``bot.groups.tag_bind(...)``
     - ``GroupsTagBind``
     - ``group_id``, ``tag_id``, ``user_id``, ``act``
   * - `groups.tagDelete <https://dev.vk.com/method/groups.tagDelete>`__
     - ``bot.groups.tag_delete(...)``
     - ``GroupsTagDelete``
     - ``group_id``, ``tag_id``
   * - `groups.tagUpdate <https://dev.vk.com/method/groups.tagUpdate>`__
     - ``bot.groups.tag_update(...)``
     - ``GroupsTagUpdate``
     - ``group_id``, ``tag_id``, ``tag_name``
   * - `groups.toggleMarket <https://dev.vk.com/method/groups.toggleMarket>`__
     - ``bot.groups.toggle_market(...)``
     - ``GroupsToggleMarket``
     - ``group_id``, ``state``
   * - `groups.unban <https://dev.vk.com/method/groups.unban>`__
     - ``bot.groups.unban(...)``
     - ``GroupsUnban``
     - ``group_id``

leadForms
~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `leadForms.create <https://dev.vk.com/method/leadForms.create>`__
     - ``bot.leadForms.create(...)``
     - ``LeadFormsCreate``
     - ``group_id``, ``name``, ``title``, ``description``, ``questions``, ``policy_link_url``
   * - `leadForms.delete <https://dev.vk.com/method/leadForms.delete>`__
     - ``bot.leadForms.delete(...)``
     - ``LeadFormsDelete``
     - ``group_id``, ``form_id``
   * - `leadForms.get <https://dev.vk.com/method/leadForms.get>`__
     - ``bot.leadForms.get(...)``
     - ``LeadFormsGet``
     - ``group_id``, ``form_id``
   * - `leadForms.getLeads <https://dev.vk.com/method/leadForms.getLeads>`__
     - ``bot.leadForms.get_leads(...)``
     - ``LeadFormsGetLeads``
     - ``group_id``, ``form_id``
   * - `leadForms.getUploadURL <https://dev.vk.com/method/leadForms.getUploadURL>`__
     - ``bot.leadForms.get_upload_u_r_l(...)``
     - ``LeadFormsGetUploadURL``
     - нет
   * - `leadForms.list <https://dev.vk.com/method/leadForms.list>`__
     - ``bot.leadForms.list(...)``
     - ``LeadFormsList``
     - ``group_id``
   * - `leadForms.update <https://dev.vk.com/method/leadForms.update>`__
     - ``bot.leadForms.update(...)``
     - ``LeadFormsUpdate``
     - ``group_id``, ``form_id``, ``name``, ``title``, ``description``, ``questions``, ``policy_link_url``

likes
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `likes.add <https://dev.vk.com/method/likes.add>`__
     - ``bot.likes.add(...)``
     - ``LikesAdd``
     - ``type``, ``item_id``
   * - `likes.delete <https://dev.vk.com/method/likes.delete>`__
     - ``bot.likes.delete(...)``
     - ``LikesDelete``
     - ``type``, ``item_id``
   * - `likes.getList <https://dev.vk.com/method/likes.getList>`__
     - ``bot.likes.get_list(...)``
     - ``LikesGetList``
     - ``type``
   * - `likes.isLiked <https://dev.vk.com/method/likes.isLiked>`__
     - ``bot.likes.is_liked(...)``
     - ``LikesIsLiked``
     - ``type``, ``item_id``

market
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `market.add <https://dev.vk.com/method/market.add>`__
     - ``bot.market.add(...)``
     - ``MarketAdd``
     - ``owner_id``, ``name``, ``description``, ``category_id``
   * - `market.addAlbum <https://dev.vk.com/method/market.addAlbum>`__
     - ``bot.market.add_album(...)``
     - ``MarketAddAlbum``
     - ``owner_id``, ``title``
   * - `market.addProperty <https://dev.vk.com/method/market.addProperty>`__
     - ``bot.market.add_property(...)``
     - ``MarketAddProperty``
     - ``group_id``, ``title``
   * - `market.addPropertyVariant <https://dev.vk.com/method/market.addPropertyVariant>`__
     - ``bot.market.add_property_variant(...)``
     - ``MarketAddPropertyVariant``
     - ``group_id``, ``property_id``, ``title``
   * - `market.addToAlbum <https://dev.vk.com/method/market.addToAlbum>`__
     - ``bot.market.add_to_album(...)``
     - ``MarketAddToAlbum``
     - ``owner_id``, ``item_ids``, ``album_ids``
   * - `market.createComment <https://dev.vk.com/method/market.createComment>`__
     - ``bot.market.create_comment(...)``
     - ``MarketCreateComment``
     - ``owner_id``, ``item_id``
   * - `market.delete <https://dev.vk.com/method/market.delete>`__
     - ``bot.market.delete(...)``
     - ``MarketDelete``
     - ``owner_id``, ``item_id``
   * - `market.deleteAlbum <https://dev.vk.com/method/market.deleteAlbum>`__
     - ``bot.market.delete_album(...)``
     - ``MarketDeleteAlbum``
     - ``owner_id``, ``album_id``
   * - `market.deleteComment <https://dev.vk.com/method/market.deleteComment>`__
     - ``bot.market.delete_comment(...)``
     - ``MarketDeleteComment``
     - ``owner_id``, ``comment_id``
   * - `market.deleteProperty <https://dev.vk.com/method/market.deleteProperty>`__
     - ``bot.market.delete_property(...)``
     - ``MarketDeleteProperty``
     - ``group_id``, ``property_id``
   * - `market.deletePropertyVariant <https://dev.vk.com/method/market.deletePropertyVariant>`__
     - ``bot.market.delete_property_variant(...)``
     - ``MarketDeletePropertyVariant``
     - ``group_id``, ``variant_id``
   * - `market.edit <https://dev.vk.com/method/market.edit>`__
     - ``bot.market.edit(...)``
     - ``MarketEdit``
     - ``owner_id``, ``item_id``
   * - `market.editAlbum <https://dev.vk.com/method/market.editAlbum>`__
     - ``bot.market.edit_album(...)``
     - ``MarketEditAlbum``
     - ``owner_id``, ``album_id``, ``title``
   * - `market.editComment <https://dev.vk.com/method/market.editComment>`__
     - ``bot.market.edit_comment(...)``
     - ``MarketEditComment``
     - ``owner_id``, ``comment_id``
   * - `market.editOrder <https://dev.vk.com/method/market.editOrder>`__
     - ``bot.market.edit_order(...)``
     - ``MarketEditOrder``
     - ``user_id``, ``order_id``
   * - `market.editProperty <https://dev.vk.com/method/market.editProperty>`__
     - ``bot.market.edit_property(...)``
     - ``MarketEditProperty``
     - ``group_id``, ``property_id``, ``title``
   * - `market.editPropertyVariant <https://dev.vk.com/method/market.editPropertyVariant>`__
     - ``bot.market.edit_property_variant(...)``
     - ``MarketEditPropertyVariant``
     - ``group_id``, ``variant_id``, ``title``
   * - `market.filterCategories <https://dev.vk.com/method/market.filterCategories>`__
     - ``bot.market.filter_categories(...)``
     - ``MarketFilterCategories``
     - нет
   * - `market.get <https://dev.vk.com/method/market.get>`__
     - ``bot.market.get(...)``
     - ``MarketGet``
     - ``owner_id``
   * - `market.getAlbumById <https://dev.vk.com/method/market.getAlbumById>`__
     - ``bot.market.get_album_by_id(...)``
     - ``MarketGetAlbumById``
     - ``owner_id``, ``album_ids``
   * - `market.getAlbums <https://dev.vk.com/method/market.getAlbums>`__
     - ``bot.market.get_albums(...)``
     - ``MarketGetAlbums``
     - ``owner_id``
   * - `market.getById <https://dev.vk.com/method/market.getById>`__
     - ``bot.market.get_by_id(...)``
     - ``MarketGetById``
     - ``item_ids``
   * - `market.getCategories <https://dev.vk.com/method/market.getCategories>`__
     - ``bot.market.get_categories(...)``
     - ``MarketGetCategories``
     - нет
   * - `market.getComments <https://dev.vk.com/method/market.getComments>`__
     - ``bot.market.get_comments(...)``
     - ``MarketGetComments``
     - ``owner_id``, ``item_id``
   * - `market.getFavesForAttach <https://dev.vk.com/method/market.getFavesForAttach>`__
     - ``bot.market.get_faves_for_attach(...)``
     - ``MarketGetFavesForAttach``
     - нет
   * - `market.getGroupOrders <https://dev.vk.com/method/market.getGroupOrders>`__
     - ``bot.market.get_group_orders(...)``
     - ``MarketGetGroupOrders``
     - нет
   * - `market.getOrderById <https://dev.vk.com/method/market.getOrderById>`__
     - ``bot.market.get_order_by_id(...)``
     - ``MarketGetOrderById``
     - ``order_id``
   * - `market.getOrderItems <https://dev.vk.com/method/market.getOrderItems>`__
     - ``bot.market.get_order_items(...)``
     - ``MarketGetOrderItems``
     - ``order_id``
   * - `market.getOrders <https://dev.vk.com/method/market.getOrders>`__
     - ``bot.market.get_orders(...)``
     - ``MarketGetOrders``
     - нет
   * - `market.getProductPhotoUploadServer <https://dev.vk.com/method/market.getProductPhotoUploadServer>`__
     - ``bot.market.get_product_photo_upload_server(...)``
     - ``MarketGetProductPhotoUploadServer``
     - ``group_id``
   * - `market.getProperties <https://dev.vk.com/method/market.getProperties>`__
     - ``bot.market.get_properties(...)``
     - ``MarketGetProperties``
     - ``group_id``
   * - `market.groupItems <https://dev.vk.com/method/market.groupItems>`__
     - ``bot.market.group_items(...)``
     - ``MarketGroupItems``
     - ``group_id``, ``item_ids``
   * - `market.removeFromAlbum <https://dev.vk.com/method/market.removeFromAlbum>`__
     - ``bot.market.remove_from_album(...)``
     - ``MarketRemoveFromAlbum``
     - ``owner_id``, ``item_id``, ``album_ids``
   * - `market.reorderAlbums <https://dev.vk.com/method/market.reorderAlbums>`__
     - ``bot.market.reorder_albums(...)``
     - ``MarketReorderAlbums``
     - ``owner_id``, ``album_id``
   * - `market.reorderItems <https://dev.vk.com/method/market.reorderItems>`__
     - ``bot.market.reorder_items(...)``
     - ``MarketReorderItems``
     - ``owner_id``, ``item_id``
   * - `market.report <https://dev.vk.com/method/market.report>`__
     - ``bot.market.report(...)``
     - ``MarketReport``
     - ``owner_id``, ``item_id``
   * - `market.reportComment <https://dev.vk.com/method/market.reportComment>`__
     - ``bot.market.report_comment(...)``
     - ``MarketReportComment``
     - ``owner_id``, ``comment_id``, ``reason``
   * - `market.restore <https://dev.vk.com/method/market.restore>`__
     - ``bot.market.restore(...)``
     - ``MarketRestore``
     - ``owner_id``, ``item_id``
   * - `market.restoreComment <https://dev.vk.com/method/market.restoreComment>`__
     - ``bot.market.restore_comment(...)``
     - ``MarketRestoreComment``
     - ``owner_id``, ``comment_id``
   * - `market.saveProductPhoto <https://dev.vk.com/method/market.saveProductPhoto>`__
     - ``bot.market.save_product_photo(...)``
     - ``MarketSaveProductPhoto``
     - ``upload_response``
   * - `market.saveProductPhotoBulk <https://dev.vk.com/method/market.saveProductPhotoBulk>`__
     - ``bot.market.save_product_photo_bulk(...)``
     - ``MarketSaveProductPhotoBulk``
     - ``upload_response``
   * - `market.search <https://dev.vk.com/method/market.search>`__
     - ``bot.market.search(...)``
     - ``MarketSearch``
     - ``owner_id``
   * - `market.searchItems <https://dev.vk.com/method/market.searchItems>`__
     - ``bot.market.search_items(...)``
     - ``MarketSearchItems``
     - ``q``
   * - `market.searchItemsBasic <https://dev.vk.com/method/market.searchItemsBasic>`__
     - ``bot.market.search_items_basic(...)``
     - ``MarketSearchItemsBasic``
     - ``q``
   * - `market.ungroupItems <https://dev.vk.com/method/market.ungroupItems>`__
     - ``bot.market.ungroup_items(...)``
     - ``MarketUngroupItems``
     - ``group_id``, ``item_group_id``

messages
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `messages.addChatUser <https://dev.vk.com/method/messages.addChatUser>`__
     - ``bot.messages.add_chat_user(...)``
     - ``MessagesAddChatUser``
     - ``chat_id``
   * - `messages.addChatUsers <https://dev.vk.com/method/messages.addChatUsers>`__
     - ``bot.messages.add_chat_users(...)``
     - ``MessagesAddChatUsers``
     - нет
   * - `messages.allowMessagesFromGroup <https://dev.vk.com/method/messages.allowMessagesFromGroup>`__
     - ``bot.messages.allow_messages_from_group(...)``
     - ``MessagesAllowMessagesFromGroup``
     - ``group_id``
   * - `messages.createChat <https://dev.vk.com/method/messages.createChat>`__
     - ``bot.messages.create_chat(...)``
     - ``MessagesCreateChat``
     - нет
   * - `messages.delete <https://dev.vk.com/method/messages.delete>`__
     - ``bot.messages.delete(...)``
     - ``MessagesDelete``
     - нет
   * - `messages.deleteChatPhoto <https://dev.vk.com/method/messages.deleteChatPhoto>`__
     - ``bot.messages.delete_chat_photo(...)``
     - ``MessagesDeleteChatPhoto``
     - ``chat_id``
   * - `messages.deleteConversation <https://dev.vk.com/method/messages.deleteConversation>`__
     - ``bot.messages.delete_conversation(...)``
     - ``MessagesDeleteConversation``
     - нет
   * - `messages.deleteReaction <https://dev.vk.com/method/messages.deleteReaction>`__
     - ``bot.messages.delete_reaction(...)``
     - ``MessagesDeleteReaction``
     - ``peer_id``, ``cmid``
   * - `messages.denyMessagesFromGroup <https://dev.vk.com/method/messages.denyMessagesFromGroup>`__
     - ``bot.messages.deny_messages_from_group(...)``
     - ``MessagesDenyMessagesFromGroup``
     - ``group_id``
   * - `messages.edit <https://dev.vk.com/method/messages.edit>`__
     - ``bot.messages.edit(...)``
     - ``MessagesEdit``
     - ``peer_id``
   * - `messages.editChat <https://dev.vk.com/method/messages.editChat>`__
     - ``bot.messages.edit_chat(...)``
     - ``MessagesEditChat``
     - ``chat_id``
   * - `messages.getByConversationMessageId <https://dev.vk.com/method/messages.getByConversationMessageId>`__
     - ``bot.messages.get_by_conversation_message_id(...)``
     - ``MessagesGetByConversationMessageId``
     - ``peer_id``, ``conversation_message_ids``
   * - `messages.getById <https://dev.vk.com/method/messages.getById>`__
     - ``bot.messages.get_by_id(...)``
     - ``MessagesGetById``
     - нет
   * - `messages.getChat <https://dev.vk.com/method/messages.getChat>`__
     - ``bot.messages.get_chat(...)``
     - ``MessagesGetChat``
     - нет
   * - `messages.getChatPreview <https://dev.vk.com/method/messages.getChatPreview>`__
     - ``bot.messages.get_chat_preview(...)``
     - ``MessagesGetChatPreview``
     - нет
   * - `messages.getConversationMembers <https://dev.vk.com/method/messages.getConversationMembers>`__
     - ``bot.messages.get_conversation_members(...)``
     - ``MessagesGetConversationMembers``
     - ``peer_id``
   * - `messages.getConversations <https://dev.vk.com/method/messages.getConversations>`__
     - ``bot.messages.get_conversations(...)``
     - ``MessagesGetConversations``
     - нет
   * - `messages.getConversationsById <https://dev.vk.com/method/messages.getConversationsById>`__
     - ``bot.messages.get_conversations_by_id(...)``
     - ``MessagesGetConversationsById``
     - ``peer_ids``
   * - `messages.getHistory <https://dev.vk.com/method/messages.getHistory>`__
     - ``bot.messages.get_history(...)``
     - ``MessagesGetHistory``
     - нет
   * - `messages.getHistoryAttachments <https://dev.vk.com/method/messages.getHistoryAttachments>`__
     - ``bot.messages.get_history_attachments(...)``
     - ``MessagesGetHistoryAttachments``
     - нет
   * - `messages.getImportantMessages <https://dev.vk.com/method/messages.getImportantMessages>`__
     - ``bot.messages.get_important_messages(...)``
     - ``MessagesGetImportantMessages``
     - нет
   * - `messages.getIntentUsers <https://dev.vk.com/method/messages.getIntentUsers>`__
     - ``bot.messages.get_intent_users(...)``
     - ``MessagesGetIntentUsers``
     - ``intent``
   * - `messages.getInviteLink <https://dev.vk.com/method/messages.getInviteLink>`__
     - ``bot.messages.get_invite_link(...)``
     - ``MessagesGetInviteLink``
     - ``peer_id``
   * - `messages.getLastActivity <https://dev.vk.com/method/messages.getLastActivity>`__
     - ``bot.messages.get_last_activity(...)``
     - ``MessagesGetLastActivity``
     - ``user_id``
   * - `messages.getLongPollHistory <https://dev.vk.com/method/messages.getLongPollHistory>`__
     - ``bot.messages.get_long_poll_history(...)``
     - ``MessagesGetLongPollHistory``
     - нет
   * - `messages.getLongPollServer <https://dev.vk.com/method/messages.getLongPollServer>`__
     - ``bot.messages.get_long_poll_server(...)``
     - ``MessagesGetLongPollServer``
     - нет
   * - `messages.getMessagesReactions <https://dev.vk.com/method/messages.getMessagesReactions>`__
     - ``bot.messages.get_messages_reactions(...)``
     - ``MessagesGetMessagesReactions``
     - ``peer_id``, ``cmids``
   * - `messages.getReactedPeers <https://dev.vk.com/method/messages.getReactedPeers>`__
     - ``bot.messages.get_reacted_peers(...)``
     - ``MessagesGetReactedPeers``
     - ``peer_id``, ``cmid``
   * - `messages.getReactionsAssets <https://dev.vk.com/method/messages.getReactionsAssets>`__
     - ``bot.messages.get_reactions_assets(...)``
     - ``MessagesGetReactionsAssets``
     - нет
   * - `messages.isMessagesFromGroupAllowed <https://dev.vk.com/method/messages.isMessagesFromGroupAllowed>`__
     - ``bot.messages.is_messages_from_group_allowed(...)``
     - ``MessagesIsMessagesFromGroupAllowed``
     - ``group_id``, ``user_id``
   * - `messages.joinChatByInviteLink <https://dev.vk.com/method/messages.joinChatByInviteLink>`__
     - ``bot.messages.join_chat_by_invite_link(...)``
     - ``MessagesJoinChatByInviteLink``
     - ``link``
   * - `messages.markAsAnsweredConversation <https://dev.vk.com/method/messages.markAsAnsweredConversation>`__
     - ``bot.messages.mark_as_answered_conversation(...)``
     - ``MessagesMarkAsAnsweredConversation``
     - ``peer_id``
   * - `messages.markAsImportant <https://dev.vk.com/method/messages.markAsImportant>`__
     - ``bot.messages.mark_as_important(...)``
     - ``MessagesMarkAsImportant``
     - нет
   * - `messages.markAsImportantConversation <https://dev.vk.com/method/messages.markAsImportantConversation>`__
     - ``bot.messages.mark_as_important_conversation(...)``
     - ``MessagesMarkAsImportantConversation``
     - ``peer_id``
   * - `messages.markAsRead <https://dev.vk.com/method/messages.markAsRead>`__
     - ``bot.messages.mark_as_read(...)``
     - ``MessagesMarkAsRead``
     - нет
   * - `messages.markReactionsAsRead <https://dev.vk.com/method/messages.markReactionsAsRead>`__
     - ``bot.messages.mark_reactions_as_read(...)``
     - ``MessagesMarkReactionsAsRead``
     - ``peer_id``
   * - `messages.muteChatMentions <https://dev.vk.com/method/messages.muteChatMentions>`__
     - ``bot.messages.mute_chat_mentions(...)``
     - ``MessagesMuteChatMentions``
     - ``peer_id``, ``mention_status``
   * - `messages.pin <https://dev.vk.com/method/messages.pin>`__
     - ``bot.messages.pin(...)``
     - ``MessagesPin``
     - ``peer_id``
   * - `messages.removeChatUser <https://dev.vk.com/method/messages.removeChatUser>`__
     - ``bot.messages.remove_chat_user(...)``
     - ``MessagesRemoveChatUser``
     - ``chat_id``
   * - `messages.restore <https://dev.vk.com/method/messages.restore>`__
     - ``bot.messages.restore(...)``
     - ``MessagesRestore``
     - нет
   * - `messages.search <https://dev.vk.com/method/messages.search>`__
     - ``bot.messages.search(...)``
     - ``MessagesSearch``
     - нет
   * - `messages.searchConversations <https://dev.vk.com/method/messages.searchConversations>`__
     - ``bot.messages.search_conversations(...)``
     - ``MessagesSearchConversations``
     - нет
   * - `messages.send <https://dev.vk.com/method/messages.send>`__
     - ``bot.messages.send(...)``
     - ``MessagesSend``
     - нет
   * - `messages.sendMessageEventAnswer <https://dev.vk.com/method/messages.sendMessageEventAnswer>`__
     - ``bot.messages.send_message_event_answer(...)``
     - ``MessagesSendMessageEventAnswer``
     - ``event_id``, ``user_id``, ``peer_id``
   * - `messages.sendReaction <https://dev.vk.com/method/messages.sendReaction>`__
     - ``bot.messages.send_reaction(...)``
     - ``MessagesSendReaction``
     - ``peer_id``, ``cmid``, ``reaction_id``
   * - `messages.setActivity <https://dev.vk.com/method/messages.setActivity>`__
     - ``bot.messages.set_activity(...)``
     - ``MessagesSetActivity``
     - нет
   * - `messages.setChatPhoto <https://dev.vk.com/method/messages.setChatPhoto>`__
     - ``bot.messages.set_chat_photo(...)``
     - ``MessagesSetChatPhoto``
     - ``file``
   * - `messages.unpin <https://dev.vk.com/method/messages.unpin>`__
     - ``bot.messages.unpin(...)``
     - ``MessagesUnpin``
     - ``peer_id``

newsfeed
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `newsfeed.addBan <https://dev.vk.com/method/newsfeed.addBan>`__
     - ``bot.newsfeed.add_ban(...)``
     - ``NewsfeedAddBan``
     - нет
   * - `newsfeed.deleteBan <https://dev.vk.com/method/newsfeed.deleteBan>`__
     - ``bot.newsfeed.delete_ban(...)``
     - ``NewsfeedDeleteBan``
     - нет
   * - `newsfeed.deleteList <https://dev.vk.com/method/newsfeed.deleteList>`__
     - ``bot.newsfeed.delete_list(...)``
     - ``NewsfeedDeleteList``
     - ``list_id``
   * - `newsfeed.get <https://dev.vk.com/method/newsfeed.get>`__
     - ``bot.newsfeed.get(...)``
     - ``NewsfeedGet``
     - нет
   * - `newsfeed.getBanned <https://dev.vk.com/method/newsfeed.getBanned>`__
     - ``bot.newsfeed.get_banned(...)``
     - ``NewsfeedGetBanned``
     - нет
   * - `newsfeed.getComments <https://dev.vk.com/method/newsfeed.getComments>`__
     - ``bot.newsfeed.get_comments(...)``
     - ``NewsfeedGetComments``
     - нет
   * - `newsfeed.getLists <https://dev.vk.com/method/newsfeed.getLists>`__
     - ``bot.newsfeed.get_lists(...)``
     - ``NewsfeedGetLists``
     - нет
   * - `newsfeed.getMentions <https://dev.vk.com/method/newsfeed.getMentions>`__
     - ``bot.newsfeed.get_mentions(...)``
     - ``NewsfeedGetMentions``
     - нет
   * - `newsfeed.getRecommended <https://dev.vk.com/method/newsfeed.getRecommended>`__
     - ``bot.newsfeed.get_recommended(...)``
     - ``NewsfeedGetRecommended``
     - нет
   * - `newsfeed.getSuggestedSources <https://dev.vk.com/method/newsfeed.getSuggestedSources>`__
     - ``bot.newsfeed.get_suggested_sources(...)``
     - ``NewsfeedGetSuggestedSources``
     - нет
   * - `newsfeed.ignoreItem <https://dev.vk.com/method/newsfeed.ignoreItem>`__
     - ``bot.newsfeed.ignore_item(...)``
     - ``NewsfeedIgnoreItem``
     - ``type``
   * - `newsfeed.saveList <https://dev.vk.com/method/newsfeed.saveList>`__
     - ``bot.newsfeed.save_list(...)``
     - ``NewsfeedSaveList``
     - ``title``, ``source_ids``
   * - `newsfeed.search <https://dev.vk.com/method/newsfeed.search>`__
     - ``bot.newsfeed.search(...)``
     - ``NewsfeedSearch``
     - нет
   * - `newsfeed.unignoreItem <https://dev.vk.com/method/newsfeed.unignoreItem>`__
     - ``bot.newsfeed.unignore_item(...)``
     - ``NewsfeedUnignoreItem``
     - ``type``
   * - `newsfeed.unsubscribe <https://dev.vk.com/method/newsfeed.unsubscribe>`__
     - ``bot.newsfeed.unsubscribe(...)``
     - ``NewsfeedUnsubscribe``
     - ``type``, ``item_id``

notes
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `notes.add <https://dev.vk.com/method/notes.add>`__
     - ``bot.notes.add(...)``
     - ``NotesAdd``
     - ``title``, ``text``
   * - `notes.createComment <https://dev.vk.com/method/notes.createComment>`__
     - ``bot.notes.create_comment(...)``
     - ``NotesCreateComment``
     - ``note_id``, ``message``
   * - `notes.delete <https://dev.vk.com/method/notes.delete>`__
     - ``bot.notes.delete(...)``
     - ``NotesDelete``
     - ``note_id``
   * - `notes.deleteComment <https://dev.vk.com/method/notes.deleteComment>`__
     - ``bot.notes.delete_comment(...)``
     - ``NotesDeleteComment``
     - ``comment_id``
   * - `notes.edit <https://dev.vk.com/method/notes.edit>`__
     - ``bot.notes.edit(...)``
     - ``NotesEdit``
     - ``note_id``, ``title``, ``text``
   * - `notes.editComment <https://dev.vk.com/method/notes.editComment>`__
     - ``bot.notes.edit_comment(...)``
     - ``NotesEditComment``
     - ``comment_id``, ``message``
   * - `notes.get <https://dev.vk.com/method/notes.get>`__
     - ``bot.notes.get(...)``
     - ``NotesGet``
     - нет
   * - `notes.getById <https://dev.vk.com/method/notes.getById>`__
     - ``bot.notes.get_by_id(...)``
     - ``NotesGetById``
     - ``note_id``
   * - `notes.getComments <https://dev.vk.com/method/notes.getComments>`__
     - ``bot.notes.get_comments(...)``
     - ``NotesGetComments``
     - ``note_id``
   * - `notes.restoreComment <https://dev.vk.com/method/notes.restoreComment>`__
     - ``bot.notes.restore_comment(...)``
     - ``NotesRestoreComment``
     - ``comment_id``

notifications
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `notifications.get <https://dev.vk.com/method/notifications.get>`__
     - ``bot.notifications.get(...)``
     - ``NotificationsGet``
     - нет
   * - `notifications.markAsViewed <https://dev.vk.com/method/notifications.markAsViewed>`__
     - ``bot.notifications.mark_as_viewed(...)``
     - ``NotificationsMarkAsViewed``
     - нет
   * - `notifications.sendMessage <https://dev.vk.com/method/notifications.sendMessage>`__
     - ``bot.notifications.send_message(...)``
     - ``NotificationsSendMessage``
     - ``user_ids``, ``message``

orders
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `orders.cancelSubscription <https://dev.vk.com/method/orders.cancelSubscription>`__
     - ``bot.orders.cancel_subscription(...)``
     - ``OrdersCancelSubscription``
     - ``user_id``, ``subscription_id``
   * - `orders.changeState <https://dev.vk.com/method/orders.changeState>`__
     - ``bot.orders.change_state(...)``
     - ``OrdersChangeState``
     - ``order_id``, ``action``
   * - `orders.get <https://dev.vk.com/method/orders.get>`__
     - ``bot.orders.get(...)``
     - ``OrdersGet``
     - нет
   * - `orders.getAmount <https://dev.vk.com/method/orders.getAmount>`__
     - ``bot.orders.get_amount(...)``
     - ``OrdersGetAmount``
     - ``user_id``, ``votes``
   * - `orders.getById <https://dev.vk.com/method/orders.getById>`__
     - ``bot.orders.get_by_id(...)``
     - ``OrdersGetById``
     - нет
   * - `orders.getUserSubscriptionById <https://dev.vk.com/method/orders.getUserSubscriptionById>`__
     - ``bot.orders.get_user_subscription_by_id(...)``
     - ``OrdersGetUserSubscriptionById``
     - ``user_id``, ``subscription_id``
   * - `orders.getUserSubscriptions <https://dev.vk.com/method/orders.getUserSubscriptions>`__
     - ``bot.orders.get_user_subscriptions(...)``
     - ``OrdersGetUserSubscriptions``
     - ``user_id``

pages
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `pages.clearCache <https://dev.vk.com/method/pages.clearCache>`__
     - ``bot.pages.clear_cache(...)``
     - ``PagesClearCache``
     - ``url``
   * - `pages.get <https://dev.vk.com/method/pages.get>`__
     - ``bot.pages.get(...)``
     - ``PagesGet``
     - нет
   * - `pages.getHistory <https://dev.vk.com/method/pages.getHistory>`__
     - ``bot.pages.get_history(...)``
     - ``PagesGetHistory``
     - ``page_id``
   * - `pages.getTitles <https://dev.vk.com/method/pages.getTitles>`__
     - ``bot.pages.get_titles(...)``
     - ``PagesGetTitles``
     - нет
   * - `pages.getVersion <https://dev.vk.com/method/pages.getVersion>`__
     - ``bot.pages.get_version(...)``
     - ``PagesGetVersion``
     - ``version_id``
   * - `pages.parseWiki <https://dev.vk.com/method/pages.parseWiki>`__
     - ``bot.pages.parse_wiki(...)``
     - ``PagesParseWiki``
     - ``text``
   * - `pages.save <https://dev.vk.com/method/pages.save>`__
     - ``bot.pages.save(...)``
     - ``PagesSave``
     - нет
   * - `pages.saveAccess <https://dev.vk.com/method/pages.saveAccess>`__
     - ``bot.pages.save_access(...)``
     - ``PagesSaveAccess``
     - ``page_id``

photos
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `photos.confirmTag <https://dev.vk.com/method/photos.confirmTag>`__
     - ``bot.photos.confirm_tag(...)``
     - ``PhotosConfirmTag``
     - ``photo_id``, ``tag_id``
   * - `photos.copy <https://dev.vk.com/method/photos.copy>`__
     - ``bot.photos.copy(...)``
     - ``PhotosCopy``
     - ``owner_id``, ``photo_id``
   * - `photos.createAlbum <https://dev.vk.com/method/photos.createAlbum>`__
     - ``bot.photos.create_album(...)``
     - ``PhotosCreateAlbum``
     - ``title``
   * - `photos.createComment <https://dev.vk.com/method/photos.createComment>`__
     - ``bot.photos.create_comment(...)``
     - ``PhotosCreateComment``
     - ``photo_id``
   * - `photos.delete <https://dev.vk.com/method/photos.delete>`__
     - ``bot.photos.delete(...)``
     - ``PhotosDelete``
     - нет
   * - `photos.deleteAlbum <https://dev.vk.com/method/photos.deleteAlbum>`__
     - ``bot.photos.delete_album(...)``
     - ``PhotosDeleteAlbum``
     - ``album_id``
   * - `photos.deleteComment <https://dev.vk.com/method/photos.deleteComment>`__
     - ``bot.photos.delete_comment(...)``
     - ``PhotosDeleteComment``
     - ``comment_id``
   * - `photos.edit <https://dev.vk.com/method/photos.edit>`__
     - ``bot.photos.edit(...)``
     - ``PhotosEdit``
     - ``photo_id``
   * - `photos.editAlbum <https://dev.vk.com/method/photos.editAlbum>`__
     - ``bot.photos.edit_album(...)``
     - ``PhotosEditAlbum``
     - ``album_id``
   * - `photos.editComment <https://dev.vk.com/method/photos.editComment>`__
     - ``bot.photos.edit_comment(...)``
     - ``PhotosEditComment``
     - ``comment_id``
   * - `photos.get <https://dev.vk.com/method/photos.get>`__
     - ``bot.photos.get(...)``
     - ``PhotosGet``
     - нет
   * - `photos.getAlbums <https://dev.vk.com/method/photos.getAlbums>`__
     - ``bot.photos.get_albums(...)``
     - ``PhotosGetAlbums``
     - нет
   * - `photos.getAlbumsCount <https://dev.vk.com/method/photos.getAlbumsCount>`__
     - ``bot.photos.get_albums_count(...)``
     - ``PhotosGetAlbumsCount``
     - нет
   * - `photos.getAll <https://dev.vk.com/method/photos.getAll>`__
     - ``bot.photos.get_all(...)``
     - ``PhotosGetAll``
     - нет
   * - `photos.getAllComments <https://dev.vk.com/method/photos.getAllComments>`__
     - ``bot.photos.get_all_comments(...)``
     - ``PhotosGetAllComments``
     - нет
   * - `photos.getById <https://dev.vk.com/method/photos.getById>`__
     - ``bot.photos.get_by_id(...)``
     - ``PhotosGetById``
     - ``photos``
   * - `photos.getChatUploadServer <https://dev.vk.com/method/photos.getChatUploadServer>`__
     - ``bot.photos.get_chat_upload_server(...)``
     - ``PhotosGetChatUploadServer``
     - ``chat_id``
   * - `photos.getComments <https://dev.vk.com/method/photos.getComments>`__
     - ``bot.photos.get_comments(...)``
     - ``PhotosGetComments``
     - ``photo_id``
   * - `photos.getMarketAlbumUploadServer <https://dev.vk.com/method/photos.getMarketAlbumUploadServer>`__
     - ``bot.photos.get_market_album_upload_server(...)``
     - ``PhotosGetMarketAlbumUploadServer``
     - ``group_id``
   * - `photos.getMessagesUploadServer <https://dev.vk.com/method/photos.getMessagesUploadServer>`__
     - ``bot.photos.get_messages_upload_server(...)``
     - ``PhotosGetMessagesUploadServer``
     - нет
   * - `photos.getNewTags <https://dev.vk.com/method/photos.getNewTags>`__
     - ``bot.photos.get_new_tags(...)``
     - ``PhotosGetNewTags``
     - нет
   * - `photos.getOwnerCoverPhotoUploadServer <https://dev.vk.com/method/photos.getOwnerCoverPhotoUploadServer>`__
     - ``bot.photos.get_owner_cover_photo_upload_server(...)``
     - ``PhotosGetOwnerCoverPhotoUploadServer``
     - нет
   * - `photos.getOwnerPhotoUploadServer <https://dev.vk.com/method/photos.getOwnerPhotoUploadServer>`__
     - ``bot.photos.get_owner_photo_upload_server(...)``
     - ``PhotosGetOwnerPhotoUploadServer``
     - нет
   * - `photos.getTags <https://dev.vk.com/method/photos.getTags>`__
     - ``bot.photos.get_tags(...)``
     - ``PhotosGetTags``
     - ``photo_id``
   * - `photos.getUploadServer <https://dev.vk.com/method/photos.getUploadServer>`__
     - ``bot.photos.get_upload_server(...)``
     - ``PhotosGetUploadServer``
     - нет
   * - `photos.getUserPhotos <https://dev.vk.com/method/photos.getUserPhotos>`__
     - ``bot.photos.get_user_photos(...)``
     - ``PhotosGetUserPhotos``
     - нет
   * - `photos.getWallUploadServer <https://dev.vk.com/method/photos.getWallUploadServer>`__
     - ``bot.photos.get_wall_upload_server(...)``
     - ``PhotosGetWallUploadServer``
     - нет
   * - `photos.makeCover <https://dev.vk.com/method/photos.makeCover>`__
     - ``bot.photos.make_cover(...)``
     - ``PhotosMakeCover``
     - ``photo_id``
   * - `photos.move <https://dev.vk.com/method/photos.move>`__
     - ``bot.photos.move(...)``
     - ``PhotosMove``
     - ``target_album_id``, ``photo_ids``
   * - `photos.putTag <https://dev.vk.com/method/photos.putTag>`__
     - ``bot.photos.put_tag(...)``
     - ``PhotosPutTag``
     - ``photo_id``, ``user_id``
   * - `photos.removeTag <https://dev.vk.com/method/photos.removeTag>`__
     - ``bot.photos.remove_tag(...)``
     - ``PhotosRemoveTag``
     - ``photo_id``, ``tag_id``
   * - `photos.reorderAlbums <https://dev.vk.com/method/photos.reorderAlbums>`__
     - ``bot.photos.reorder_albums(...)``
     - ``PhotosReorderAlbums``
     - ``album_id``
   * - `photos.reorderPhotos <https://dev.vk.com/method/photos.reorderPhotos>`__
     - ``bot.photos.reorder_photos(...)``
     - ``PhotosReorderPhotos``
     - ``photo_id``
   * - `photos.report <https://dev.vk.com/method/photos.report>`__
     - ``bot.photos.report(...)``
     - ``PhotosReport``
     - ``owner_id``, ``photo_id``
   * - `photos.reportComment <https://dev.vk.com/method/photos.reportComment>`__
     - ``bot.photos.report_comment(...)``
     - ``PhotosReportComment``
     - ``owner_id``, ``comment_id``
   * - `photos.restore <https://dev.vk.com/method/photos.restore>`__
     - ``bot.photos.restore(...)``
     - ``PhotosRestore``
     - ``photo_id``
   * - `photos.restoreComment <https://dev.vk.com/method/photos.restoreComment>`__
     - ``bot.photos.restore_comment(...)``
     - ``PhotosRestoreComment``
     - ``comment_id``
   * - `photos.save <https://dev.vk.com/method/photos.save>`__
     - ``bot.photos.save(...)``
     - ``PhotosSave``
     - нет
   * - `photos.saveMarketAlbumPhoto <https://dev.vk.com/method/photos.saveMarketAlbumPhoto>`__
     - ``bot.photos.save_market_album_photo(...)``
     - ``PhotosSaveMarketAlbumPhoto``
     - ``group_id``, ``photo``, ``server``, ``hash``
   * - `photos.saveMessagesPhoto <https://dev.vk.com/method/photos.saveMessagesPhoto>`__
     - ``bot.photos.save_messages_photo(...)``
     - ``PhotosSaveMessagesPhoto``
     - ``photo``
   * - `photos.saveOwnerCoverPhoto <https://dev.vk.com/method/photos.saveOwnerCoverPhoto>`__
     - ``bot.photos.save_owner_cover_photo(...)``
     - ``PhotosSaveOwnerCoverPhoto``
     - нет
   * - `photos.saveOwnerPhoto <https://dev.vk.com/method/photos.saveOwnerPhoto>`__
     - ``bot.photos.save_owner_photo(...)``
     - ``PhotosSaveOwnerPhoto``
     - нет
   * - `photos.saveWallPhoto <https://dev.vk.com/method/photos.saveWallPhoto>`__
     - ``bot.photos.save_wall_photo(...)``
     - ``PhotosSaveWallPhoto``
     - ``photo``
   * - `photos.search <https://dev.vk.com/method/photos.search>`__
     - ``bot.photos.search(...)``
     - ``PhotosSearch``
     - нет

podcasts
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `podcasts.searchPodcast <https://dev.vk.com/method/podcasts.searchPodcast>`__
     - ``bot.podcasts.search_podcast(...)``
     - ``PodcastsSearchPodcast``
     - ``search_string``

polls
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `polls.addVote <https://dev.vk.com/method/polls.addVote>`__
     - ``bot.polls.add_vote(...)``
     - ``PollsAddVote``
     - ``poll_id``, ``answer_ids``
   * - `polls.create <https://dev.vk.com/method/polls.create>`__
     - ``bot.polls.create(...)``
     - ``PollsCreate``
     - нет
   * - `polls.deleteVote <https://dev.vk.com/method/polls.deleteVote>`__
     - ``bot.polls.delete_vote(...)``
     - ``PollsDeleteVote``
     - ``poll_id``
   * - `polls.edit <https://dev.vk.com/method/polls.edit>`__
     - ``bot.polls.edit(...)``
     - ``PollsEdit``
     - ``poll_id``
   * - `polls.getBackgrounds <https://dev.vk.com/method/polls.getBackgrounds>`__
     - ``bot.polls.get_backgrounds(...)``
     - ``PollsGetBackgrounds``
     - нет
   * - `polls.getById <https://dev.vk.com/method/polls.getById>`__
     - ``bot.polls.get_by_id(...)``
     - ``PollsGetById``
     - ``poll_id``
   * - `polls.getPhotoUploadServer <https://dev.vk.com/method/polls.getPhotoUploadServer>`__
     - ``bot.polls.get_photo_upload_server(...)``
     - ``PollsGetPhotoUploadServer``
     - нет
   * - `polls.getVoters <https://dev.vk.com/method/polls.getVoters>`__
     - ``bot.polls.get_voters(...)``
     - ``PollsGetVoters``
     - ``poll_id``, ``answer_ids``
   * - `polls.savePhoto <https://dev.vk.com/method/polls.savePhoto>`__
     - ``bot.polls.save_photo(...)``
     - ``PollsSavePhoto``
     - нет

prettyCards
~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `prettyCards.create <https://dev.vk.com/method/prettyCards.create>`__
     - ``bot.prettyCards.create(...)``
     - ``PrettyCardsCreate``
     - ``owner_id``, ``photo``, ``title``, ``link``
   * - `prettyCards.delete <https://dev.vk.com/method/prettyCards.delete>`__
     - ``bot.prettyCards.delete(...)``
     - ``PrettyCardsDelete``
     - ``owner_id``, ``card_id``
   * - `prettyCards.edit <https://dev.vk.com/method/prettyCards.edit>`__
     - ``bot.prettyCards.edit(...)``
     - ``PrettyCardsEdit``
     - ``owner_id``, ``card_id``
   * - `prettyCards.get <https://dev.vk.com/method/prettyCards.get>`__
     - ``bot.prettyCards.get(...)``
     - ``PrettyCardsGet``
     - ``owner_id``
   * - `prettyCards.getById <https://dev.vk.com/method/prettyCards.getById>`__
     - ``bot.prettyCards.get_by_id(...)``
     - ``PrettyCardsGetById``
     - ``owner_id``, ``card_ids``
   * - `prettyCards.getUploadURL <https://dev.vk.com/method/prettyCards.getUploadURL>`__
     - ``bot.prettyCards.get_upload_u_r_l(...)``
     - ``PrettyCardsGetUploadURL``
     - нет

search
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `search.getHints <https://dev.vk.com/method/search.getHints>`__
     - ``bot.search.get_hints(...)``
     - ``SearchGetHints``
     - нет

secure
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `secure.addAppEvent <https://dev.vk.com/method/secure.addAppEvent>`__
     - ``bot.secure.add_app_event(...)``
     - ``SecureAddAppEvent``
     - ``activity_id``
   * - `secure.checkToken <https://dev.vk.com/method/secure.checkToken>`__
     - ``bot.secure.check_token(...)``
     - ``SecureCheckToken``
     - нет
   * - `secure.getAppBalance <https://dev.vk.com/method/secure.getAppBalance>`__
     - ``bot.secure.get_app_balance(...)``
     - ``SecureGetAppBalance``
     - нет
   * - `secure.getSMSHistory <https://dev.vk.com/method/secure.getSMSHistory>`__
     - ``bot.secure.get_s_m_s_history(...)``
     - ``SecureGetSMSHistory``
     - нет
   * - `secure.getTransactionsHistory <https://dev.vk.com/method/secure.getTransactionsHistory>`__
     - ``bot.secure.get_transactions_history(...)``
     - ``SecureGetTransactionsHistory``
     - нет
   * - `secure.getUserLevel <https://dev.vk.com/method/secure.getUserLevel>`__
     - ``bot.secure.get_user_level(...)``
     - ``SecureGetUserLevel``
     - ``user_ids``
   * - `secure.giveEventSticker <https://dev.vk.com/method/secure.giveEventSticker>`__
     - ``bot.secure.give_event_sticker(...)``
     - ``SecureGiveEventSticker``
     - ``user_ids``, ``achievement_id``
   * - `secure.sendNotification <https://dev.vk.com/method/secure.sendNotification>`__
     - ``bot.secure.send_notification(...)``
     - ``SecureSendNotification``
     - ``message``
   * - `secure.sendSMSNotification <https://dev.vk.com/method/secure.sendSMSNotification>`__
     - ``bot.secure.send_s_m_s_notification(...)``
     - ``SecureSendSMSNotification``
     - ``user_id``, ``message``
   * - `secure.setCounter <https://dev.vk.com/method/secure.setCounter>`__
     - ``bot.secure.set_counter(...)``
     - ``SecureSetCounter``
     - нет

stats
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `stats.get <https://dev.vk.com/method/stats.get>`__
     - ``bot.stats.get(...)``
     - ``StatsGet``
     - нет
   * - `stats.getPostReach <https://dev.vk.com/method/stats.getPostReach>`__
     - ``bot.stats.get_post_reach(...)``
     - ``StatsGetPostReach``
     - ``owner_id``, ``post_ids``
   * - `stats.trackVisitor <https://dev.vk.com/method/stats.trackVisitor>`__
     - ``bot.stats.track_visitor(...)``
     - ``StatsTrackVisitor``
     - нет

status
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `status.get <https://dev.vk.com/method/status.get>`__
     - ``bot.status.get(...)``
     - ``StatusGet``
     - нет
   * - `status.set <https://dev.vk.com/method/status.set>`__
     - ``bot.status.set(...)``
     - ``StatusSet``
     - нет

storage
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `storage.get <https://dev.vk.com/method/storage.get>`__
     - ``bot.storage.get(...)``
     - ``StorageGet``
     - нет
   * - `storage.getKeys <https://dev.vk.com/method/storage.getKeys>`__
     - ``bot.storage.get_keys(...)``
     - ``StorageGetKeys``
     - нет
   * - `storage.set <https://dev.vk.com/method/storage.set>`__
     - ``bot.storage.set(...)``
     - ``StorageSet``
     - ``key``

store
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `store.addStickersToFavorite <https://dev.vk.com/method/store.addStickersToFavorite>`__
     - ``bot.store.add_stickers_to_favorite(...)``
     - ``StoreAddStickersToFavorite``
     - ``sticker_ids``
   * - `store.getFavoriteStickers <https://dev.vk.com/method/store.getFavoriteStickers>`__
     - ``bot.store.get_favorite_stickers(...)``
     - ``StoreGetFavoriteStickers``
     - нет
   * - `store.getProducts <https://dev.vk.com/method/store.getProducts>`__
     - ``bot.store.get_products(...)``
     - ``StoreGetProducts``
     - нет
   * - `store.getStickersKeywords <https://dev.vk.com/method/store.getStickersKeywords>`__
     - ``bot.store.get_stickers_keywords(...)``
     - ``StoreGetStickersKeywords``
     - нет
   * - `store.removeStickersFromFavorite <https://dev.vk.com/method/store.removeStickersFromFavorite>`__
     - ``bot.store.remove_stickers_from_favorite(...)``
     - ``StoreRemoveStickersFromFavorite``
     - ``sticker_ids``

stories
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `stories.banOwner <https://dev.vk.com/method/stories.banOwner>`__
     - ``bot.stories.ban_owner(...)``
     - ``StoriesBanOwner``
     - ``owners_ids``
   * - `stories.delete <https://dev.vk.com/method/stories.delete>`__
     - ``bot.stories.delete(...)``
     - ``StoriesDelete``
     - нет
   * - `stories.get <https://dev.vk.com/method/stories.get>`__
     - ``bot.stories.get(...)``
     - ``StoriesGet``
     - нет
   * - `stories.getBanned <https://dev.vk.com/method/stories.getBanned>`__
     - ``bot.stories.get_banned(...)``
     - ``StoriesGetBanned``
     - нет
   * - `stories.getById <https://dev.vk.com/method/stories.getById>`__
     - ``bot.stories.get_by_id(...)``
     - ``StoriesGetById``
     - ``stories``
   * - `stories.getPhotoUploadServer <https://dev.vk.com/method/stories.getPhotoUploadServer>`__
     - ``bot.stories.get_photo_upload_server(...)``
     - ``StoriesGetPhotoUploadServer``
     - нет
   * - `stories.getReplies <https://dev.vk.com/method/stories.getReplies>`__
     - ``bot.stories.get_replies(...)``
     - ``StoriesGetReplies``
     - ``owner_id``, ``story_id``
   * - `stories.getStats <https://dev.vk.com/method/stories.getStats>`__
     - ``bot.stories.get_stats(...)``
     - ``StoriesGetStats``
     - ``owner_id``, ``story_id``
   * - `stories.getVideoUploadServer <https://dev.vk.com/method/stories.getVideoUploadServer>`__
     - ``bot.stories.get_video_upload_server(...)``
     - ``StoriesGetVideoUploadServer``
     - нет
   * - `stories.getViewers <https://dev.vk.com/method/stories.getViewers>`__
     - ``bot.stories.get_viewers(...)``
     - ``StoriesGetViewers``
     - ``story_id``
   * - `stories.hideAllReplies <https://dev.vk.com/method/stories.hideAllReplies>`__
     - ``bot.stories.hide_all_replies(...)``
     - ``StoriesHideAllReplies``
     - ``owner_id``
   * - `stories.hideReply <https://dev.vk.com/method/stories.hideReply>`__
     - ``bot.stories.hide_reply(...)``
     - ``StoriesHideReply``
     - ``owner_id``, ``story_id``
   * - `stories.save <https://dev.vk.com/method/stories.save>`__
     - ``bot.stories.save(...)``
     - ``StoriesSave``
     - нет
   * - `stories.search <https://dev.vk.com/method/stories.search>`__
     - ``bot.stories.search(...)``
     - ``StoriesSearch``
     - нет
   * - `stories.sendInteraction <https://dev.vk.com/method/stories.sendInteraction>`__
     - ``bot.stories.send_interaction(...)``
     - ``StoriesSendInteraction``
     - ``access_key``
   * - `stories.unbanOwner <https://dev.vk.com/method/stories.unbanOwner>`__
     - ``bot.stories.unban_owner(...)``
     - ``StoriesUnbanOwner``
     - ``owners_ids``

streaming
~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `streaming.getServerUrl <https://dev.vk.com/method/streaming.getServerUrl>`__
     - ``bot.streaming.get_server_url(...)``
     - ``StreamingGetServerUrl``
     - нет
   * - `streaming.getStats <https://dev.vk.com/method/streaming.getStats>`__
     - ``bot.streaming.get_stats(...)``
     - ``StreamingGetStats``
     - нет
   * - `streaming.getStem <https://dev.vk.com/method/streaming.getStem>`__
     - ``bot.streaming.get_stem(...)``
     - ``StreamingGetStem``
     - ``word``

translations
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `translations.translate <https://dev.vk.com/method/translations.translate>`__
     - ``bot.translations.translate(...)``
     - ``TranslationsTranslate``
     - ``texts``, ``translation_language``

users
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `users.get <https://dev.vk.com/method/users.get>`__
     - ``bot.users.get(...)``
     - ``UsersGet``
     - нет
   * - `users.getFollowers <https://dev.vk.com/method/users.getFollowers>`__
     - ``bot.users.get_followers(...)``
     - ``UsersGetFollowers``
     - нет
   * - `users.getSubscriptions <https://dev.vk.com/method/users.getSubscriptions>`__
     - ``bot.users.get_subscriptions(...)``
     - ``UsersGetSubscriptions``
     - нет
   * - `users.report <https://dev.vk.com/method/users.report>`__
     - ``bot.users.report(...)``
     - ``UsersReport``
     - ``user_id``, ``type``
   * - `users.search <https://dev.vk.com/method/users.search>`__
     - ``bot.users.search(...)``
     - ``UsersSearch``
     - нет

utils
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `utils.checkLink <https://dev.vk.com/method/utils.checkLink>`__
     - ``bot.utils.check_link(...)``
     - ``UtilsCheckLink``
     - ``url``
   * - `utils.deleteFromLastShortened <https://dev.vk.com/method/utils.deleteFromLastShortened>`__
     - ``bot.utils.delete_from_last_shortened(...)``
     - ``UtilsDeleteFromLastShortened``
     - ``key``
   * - `utils.getLastShortenedLinks <https://dev.vk.com/method/utils.getLastShortenedLinks>`__
     - ``bot.utils.get_last_shortened_links(...)``
     - ``UtilsGetLastShortenedLinks``
     - нет
   * - `utils.getLinkStats <https://dev.vk.com/method/utils.getLinkStats>`__
     - ``bot.utils.get_link_stats(...)``
     - ``UtilsGetLinkStats``
     - ``key``
   * - `utils.getServerTime <https://dev.vk.com/method/utils.getServerTime>`__
     - ``bot.utils.get_server_time(...)``
     - ``UtilsGetServerTime``
     - нет
   * - `utils.getShortLink <https://dev.vk.com/method/utils.getShortLink>`__
     - ``bot.utils.get_short_link(...)``
     - ``UtilsGetShortLink``
     - ``url``
   * - `utils.resolveScreenName <https://dev.vk.com/method/utils.resolveScreenName>`__
     - ``bot.utils.resolve_screen_name(...)``
     - ``UtilsResolveScreenName``
     - ``screen_name``

video
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `video.add <https://dev.vk.com/method/video.add>`__
     - ``bot.video.add(...)``
     - ``VideoAdd``
     - ``video_id``, ``owner_id``
   * - `video.addAlbum <https://dev.vk.com/method/video.addAlbum>`__
     - ``bot.video.add_album(...)``
     - ``VideoAddAlbum``
     - нет
   * - `video.addToAlbum <https://dev.vk.com/method/video.addToAlbum>`__
     - ``bot.video.add_to_album(...)``
     - ``VideoAddToAlbum``
     - ``owner_id``, ``video_id``
   * - `video.createComment <https://dev.vk.com/method/video.createComment>`__
     - ``bot.video.create_comment(...)``
     - ``VideoCreateComment``
     - ``video_id``
   * - `video.delete <https://dev.vk.com/method/video.delete>`__
     - ``bot.video.delete(...)``
     - ``VideoDelete``
     - ``video_id``
   * - `video.deleteAlbum <https://dev.vk.com/method/video.deleteAlbum>`__
     - ``bot.video.delete_album(...)``
     - ``VideoDeleteAlbum``
     - ``album_id``
   * - `video.deleteComment <https://dev.vk.com/method/video.deleteComment>`__
     - ``bot.video.delete_comment(...)``
     - ``VideoDeleteComment``
     - ``comment_id``
   * - `video.deleteThread <https://dev.vk.com/method/video.deleteThread>`__
     - ``bot.video.delete_thread(...)``
     - ``VideoDeleteThread``
     - ``owner_id``, ``thread_id``
   * - `video.edit <https://dev.vk.com/method/video.edit>`__
     - ``bot.video.edit(...)``
     - ``VideoEdit``
     - ``video_id``
   * - `video.editAlbum <https://dev.vk.com/method/video.editAlbum>`__
     - ``bot.video.edit_album(...)``
     - ``VideoEditAlbum``
     - ``album_id``
   * - `video.editComment <https://dev.vk.com/method/video.editComment>`__
     - ``bot.video.edit_comment(...)``
     - ``VideoEditComment``
     - ``comment_id``
   * - `video.get <https://dev.vk.com/method/video.get>`__
     - ``bot.video.get(...)``
     - ``VideoGet``
     - нет
   * - `video.getAlbumById <https://dev.vk.com/method/video.getAlbumById>`__
     - ``bot.video.get_album_by_id(...)``
     - ``VideoGetAlbumById``
     - ``album_id``
   * - `video.getAlbums <https://dev.vk.com/method/video.getAlbums>`__
     - ``bot.video.get_albums(...)``
     - ``VideoGetAlbums``
     - нет
   * - `video.getAlbumsByVideo <https://dev.vk.com/method/video.getAlbumsByVideo>`__
     - ``bot.video.get_albums_by_video(...)``
     - ``VideoGetAlbumsByVideo``
     - ``owner_id``, ``video_id``
   * - `video.getComments <https://dev.vk.com/method/video.getComments>`__
     - ``bot.video.get_comments(...)``
     - ``VideoGetComments``
     - ``video_id``
   * - `video.getLongPollServer <https://dev.vk.com/method/video.getLongPollServer>`__
     - ``bot.video.get_long_poll_server(...)``
     - ``VideoGetLongPollServer``
     - ``video_id``
   * - `video.getOembed <https://dev.vk.com/method/video.getOembed>`__
     - ``bot.video.get_oembed(...)``
     - ``VideoGetOembed``
     - ``url``
   * - `video.getThumbUploadUrl <https://dev.vk.com/method/video.getThumbUploadUrl>`__
     - ``bot.video.get_thumb_upload_url(...)``
     - ``VideoGetThumbUploadUrl``
     - ``owner_id``
   * - `video.liveGetCategories <https://dev.vk.com/method/video.liveGetCategories>`__
     - ``bot.video.live_get_categories(...)``
     - ``VideoLiveGetCategories``
     - нет
   * - `video.removeFromAlbum <https://dev.vk.com/method/video.removeFromAlbum>`__
     - ``bot.video.remove_from_album(...)``
     - ``VideoRemoveFromAlbum``
     - ``owner_id``, ``video_id``
   * - `video.reorderAlbums <https://dev.vk.com/method/video.reorderAlbums>`__
     - ``bot.video.reorder_albums(...)``
     - ``VideoReorderAlbums``
     - ``album_id``
   * - `video.reorderVideos <https://dev.vk.com/method/video.reorderVideos>`__
     - ``bot.video.reorder_videos(...)``
     - ``VideoReorderVideos``
     - ``owner_id``, ``video_id``
   * - `video.report <https://dev.vk.com/method/video.report>`__
     - ``bot.video.report(...)``
     - ``VideoReport``
     - ``owner_id``, ``video_id``
   * - `video.reportComment <https://dev.vk.com/method/video.reportComment>`__
     - ``bot.video.report_comment(...)``
     - ``VideoReportComment``
     - ``owner_id``, ``comment_id``
   * - `video.restore <https://dev.vk.com/method/video.restore>`__
     - ``bot.video.restore(...)``
     - ``VideoRestore``
     - ``video_id``
   * - `video.restoreComment <https://dev.vk.com/method/video.restoreComment>`__
     - ``bot.video.restore_comment(...)``
     - ``VideoRestoreComment``
     - ``comment_id``
   * - `video.restoreThread <https://dev.vk.com/method/video.restoreThread>`__
     - ``bot.video.restore_thread(...)``
     - ``VideoRestoreThread``
     - ``owner_id``, ``thread_id``
   * - `video.save <https://dev.vk.com/method/video.save>`__
     - ``bot.video.save(...)``
     - ``VideoSave``
     - нет
   * - `video.saveUploadedThumb <https://dev.vk.com/method/video.saveUploadedThumb>`__
     - ``bot.video.save_uploaded_thumb(...)``
     - ``VideoSaveUploadedThumb``
     - ``owner_id``, ``thumb_json``
   * - `video.search <https://dev.vk.com/method/video.search>`__
     - ``bot.video.search(...)``
     - ``VideoSearch``
     - нет
   * - `video.startStreaming <https://dev.vk.com/method/video.startStreaming>`__
     - ``bot.video.start_streaming(...)``
     - ``VideoStartStreaming``
     - нет
   * - `video.stopStreaming <https://dev.vk.com/method/video.stopStreaming>`__
     - ``bot.video.stop_streaming(...)``
     - ``VideoStopStreaming``
     - нет
   * - `video.unpinComment <https://dev.vk.com/method/video.unpinComment>`__
     - ``bot.video.unpin_comment(...)``
     - ``VideoUnpinComment``
     - ``owner_id``, ``comment_id``

wall
~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `wall.checkCopyrightLink <https://dev.vk.com/method/wall.checkCopyrightLink>`__
     - ``bot.wall.check_copyright_link(...)``
     - ``WallCheckCopyrightLink``
     - ``link``
   * - `wall.closeComments <https://dev.vk.com/method/wall.closeComments>`__
     - ``bot.wall.close_comments(...)``
     - ``WallCloseComments``
     - ``owner_id``, ``post_id``
   * - `wall.createComment <https://dev.vk.com/method/wall.createComment>`__
     - ``bot.wall.create_comment(...)``
     - ``WallCreateComment``
     - ``post_id``
   * - `wall.delete <https://dev.vk.com/method/wall.delete>`__
     - ``bot.wall.delete(...)``
     - ``WallDelete``
     - нет
   * - `wall.deleteComment <https://dev.vk.com/method/wall.deleteComment>`__
     - ``bot.wall.delete_comment(...)``
     - ``WallDeleteComment``
     - ``comment_id``
   * - `wall.edit <https://dev.vk.com/method/wall.edit>`__
     - ``bot.wall.edit(...)``
     - ``WallEdit``
     - ``post_id``
   * - `wall.editAdsStealth <https://dev.vk.com/method/wall.editAdsStealth>`__
     - ``bot.wall.edit_ads_stealth(...)``
     - ``WallEditAdsStealth``
     - ``post_id``
   * - `wall.editComment <https://dev.vk.com/method/wall.editComment>`__
     - ``bot.wall.edit_comment(...)``
     - ``WallEditComment``
     - ``comment_id``
   * - `wall.get <https://dev.vk.com/method/wall.get>`__
     - ``bot.wall.get(...)``
     - ``WallGet``
     - нет
   * - `wall.getById <https://dev.vk.com/method/wall.getById>`__
     - ``bot.wall.get_by_id(...)``
     - ``WallGetById``
     - ``posts``
   * - `wall.getComment <https://dev.vk.com/method/wall.getComment>`__
     - ``bot.wall.get_comment(...)``
     - ``WallGetComment``
     - ``comment_id``
   * - `wall.getComments <https://dev.vk.com/method/wall.getComments>`__
     - ``bot.wall.get_comments(...)``
     - ``WallGetComments``
     - нет
   * - `wall.getReposts <https://dev.vk.com/method/wall.getReposts>`__
     - ``bot.wall.get_reposts(...)``
     - ``WallGetReposts``
     - нет
   * - `wall.openComments <https://dev.vk.com/method/wall.openComments>`__
     - ``bot.wall.open_comments(...)``
     - ``WallOpenComments``
     - ``owner_id``, ``post_id``
   * - `wall.parseAttachedLink <https://dev.vk.com/method/wall.parseAttachedLink>`__
     - ``bot.wall.parse_attached_link(...)``
     - ``WallParseAttachedLink``
     - ``links``
   * - `wall.pin <https://dev.vk.com/method/wall.pin>`__
     - ``bot.wall.pin(...)``
     - ``WallPin``
     - ``post_id``
   * - `wall.post <https://dev.vk.com/method/wall.post>`__
     - ``bot.wall.post(...)``
     - ``WallPost``
     - нет
   * - `wall.postAdsStealth <https://dev.vk.com/method/wall.postAdsStealth>`__
     - ``bot.wall.post_ads_stealth(...)``
     - ``WallPostAdsStealth``
     - ``owner_id``
   * - `wall.reportComment <https://dev.vk.com/method/wall.reportComment>`__
     - ``bot.wall.report_comment(...)``
     - ``WallReportComment``
     - ``owner_id``, ``comment_id``, ``reason``
   * - `wall.reportPost <https://dev.vk.com/method/wall.reportPost>`__
     - ``bot.wall.report_post(...)``
     - ``WallReportPost``
     - ``owner_id``, ``post_id``, ``reason``
   * - `wall.repost <https://dev.vk.com/method/wall.repost>`__
     - ``bot.wall.repost(...)``
     - ``WallRepost``
     - ``object``
   * - `wall.restore <https://dev.vk.com/method/wall.restore>`__
     - ``bot.wall.restore(...)``
     - ``WallRestore``
     - нет
   * - `wall.restoreComment <https://dev.vk.com/method/wall.restoreComment>`__
     - ``bot.wall.restore_comment(...)``
     - ``WallRestoreComment``
     - ``comment_id``
   * - `wall.search <https://dev.vk.com/method/wall.search>`__
     - ``bot.wall.search(...)``
     - ``WallSearch``
     - нет
   * - `wall.unpin <https://dev.vk.com/method/wall.unpin>`__
     - ``bot.wall.unpin(...)``
     - ``WallUnpin``
     - ``post_id``

widgets
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 28 26 18

   * - VK method
     - Вызов
     - Класс
     - Обязательные параметры
   * - `widgets.getComments <https://dev.vk.com/method/widgets.getComments>`__
     - ``bot.widgets.get_comments(...)``
     - ``WidgetsGetComments``
     - нет
   * - `widgets.getPages <https://dev.vk.com/method/widgets.getPages>`__
     - ``bot.widgets.get_pages(...)``
     - ``WidgetsGetPages``
     - нет
