from __future__ import annotations

from typing import Any

from pydantic import Field

from vkapi.methods.base import VKMethod


class MethodNamespace:
    def __init__(self, bot: Any) -> None:
        self._bot = bot


class AccountBan(VKMethod[Any]):
    __api_method__ = 'account.ban'
    owner_id: int | None = None

class AccountChangePassword(VKMethod[Any]):
    __api_method__ = 'account.changePassword'
    restore_sid: str | None = None
    change_password_hash: str | None = None
    old_password: str | None = None
    new_password: str = ...

class AccountGetActiveOffers(VKMethod[Any]):
    __api_method__ = 'account.getActiveOffers'
    offset: int | None = None
    count: int | None = None

class AccountGetAppPermissions(VKMethod[Any]):
    __api_method__ = 'account.getAppPermissions'
    user_id: int | None = None

class AccountGetBanned(VKMethod[Any]):
    __api_method__ = 'account.getBanned'
    offset: int | None = None
    count: int | None = None
    fields: list[Any] | None = None

class AccountGetCounters(VKMethod[Any]):
    __api_method__ = 'account.getCounters'
    filter: list[Any] | None = None

class AccountGetInfo(VKMethod[Any]):
    __api_method__ = 'account.getInfo'
    fields: list[Any] | None = None

class AccountGetProfileInfo(VKMethod[Any]):
    __api_method__ = 'account.getProfileInfo'
    pass

class AccountGetPushSettings(VKMethod[Any]):
    __api_method__ = 'account.getPushSettings'
    device_id: str | None = None

class AccountRegisterDevice(VKMethod[Any]):
    __api_method__ = 'account.registerDevice'
    token: str = ...
    device_model: str | None = None
    device_year: int | None = None
    device_id: str = ...
    system_version: str | None = None
    settings: str | None = None
    sandbox: bool | None = None
    pushes_granted: bool | None = None

class AccountSaveProfileInfo(VKMethod[Any]):
    __api_method__ = 'account.saveProfileInfo'
    first_name: str | None = None
    last_name: str | None = None
    maiden_name: str | None = None
    screen_name: str | None = None
    cancel_request_id: int | None = None
    sex: int | None = None
    relation: int | None = None
    relation_partner_id: int | None = None
    bdate: str | None = None
    bdate_visibility: int | None = None
    home_town: str | None = None
    country_id: int | None = None
    city_id: int | None = None
    status: str | None = None

class AccountSetInfo(VKMethod[Any]):
    __api_method__ = 'account.setInfo'
    name: str | None = None
    value: str | None = None

class AccountSetOffline(VKMethod[Any]):
    __api_method__ = 'account.setOffline'
    pass

class AccountSetOnline(VKMethod[Any]):
    __api_method__ = 'account.setOnline'
    voip: bool | None = None

class AccountSetPushSettings(VKMethod[Any]):
    __api_method__ = 'account.setPushSettings'
    device_id: str = ...
    settings: str | None = None
    key: str | None = None
    value: list[Any] | None = None

class AccountSetSilenceMode(VKMethod[Any]):
    __api_method__ = 'account.setSilenceMode'
    device_id: str | None = None
    time: int | None = None
    peer_id: int | None = None
    sound: int | None = None

class AccountUnban(VKMethod[Any]):
    __api_method__ = 'account.unban'
    owner_id: int | None = None

class AccountUnregisterDevice(VKMethod[Any]):
    __api_method__ = 'account.unregisterDevice'
    device_id: str | None = None
    sandbox: bool | None = None

class AdsAddOfficeUsers(VKMethod[Any]):
    __api_method__ = 'ads.addOfficeUsers'
    account_id: int = ...
    data: str = ...

class AdsCheckLink(VKMethod[Any]):
    __api_method__ = 'ads.checkLink'
    account_id: int = ...
    link_type: str = ...
    link_url: str = ...
    campaign_id: int | None = None

class AdsCreateAds(VKMethod[Any]):
    __api_method__ = 'ads.createAds'
    account_id: int = ...
    data: str = ...

class AdsCreateCampaigns(VKMethod[Any]):
    __api_method__ = 'ads.createCampaigns'
    account_id: int = ...
    data: str = ...

class AdsCreateClients(VKMethod[Any]):
    __api_method__ = 'ads.createClients'
    account_id: int = ...
    data: str = ...

class AdsCreateLookalikeRequest(VKMethod[Any]):
    __api_method__ = 'ads.createLookalikeRequest'
    account_id: int = ...
    client_id: int | None = None
    source_type: str = ...
    retargeting_group_id: int | None = None

class AdsCreateTargetGroup(VKMethod[Any]):
    __api_method__ = 'ads.createTargetGroup'
    account_id: int = ...
    client_id: int | None = None
    name: str = ...
    lifetime: int = ...
    target_pixel_id: int | None = None
    target_pixel_rules: str | None = None

class AdsCreateTargetPixel(VKMethod[Any]):
    __api_method__ = 'ads.createTargetPixel'
    account_id: int = ...
    client_id: int | None = None
    name: str = ...
    domain: str | None = None
    category_id: int = ...

class AdsDeleteAds(VKMethod[Any]):
    __api_method__ = 'ads.deleteAds'
    account_id: int = ...
    ids: str = ...

class AdsDeleteCampaigns(VKMethod[Any]):
    __api_method__ = 'ads.deleteCampaigns'
    account_id: int = ...
    ids: str = ...

class AdsDeleteClients(VKMethod[Any]):
    __api_method__ = 'ads.deleteClients'
    account_id: int = ...
    ids: str = ...

class AdsDeleteTargetGroup(VKMethod[Any]):
    __api_method__ = 'ads.deleteTargetGroup'
    account_id: int = ...
    client_id: int | None = None
    target_group_id: int = ...

class AdsDeleteTargetPixel(VKMethod[Any]):
    __api_method__ = 'ads.deleteTargetPixel'
    account_id: int = ...
    client_id: int | None = None
    target_pixel_id: int = ...

class AdsGetAccounts(VKMethod[Any]):
    __api_method__ = 'ads.getAccounts'
    pass

class AdsGetAds(VKMethod[Any]):
    __api_method__ = 'ads.getAds'
    account_id: int = ...
    client_id: int | None = None
    include_deleted: bool | None = None
    only_deleted: bool | None = None
    campaign_ids: str | None = None
    ad_ids: str | None = None
    limit: int | None = None
    offset: int | None = None

class AdsGetAdsLayout(VKMethod[Any]):
    __api_method__ = 'ads.getAdsLayout'
    account_id: int = ...
    client_id: int | None = None
    include_deleted: bool | None = None
    only_deleted: bool | None = None
    campaign_ids: str | None = None
    ad_ids: str | None = None
    limit: int | None = None
    offset: int | None = None

class AdsGetAdsTargeting(VKMethod[Any]):
    __api_method__ = 'ads.getAdsTargeting'
    account_id: int = ...
    client_id: int | None = None
    include_deleted: bool | None = None
    only_deleted: bool | None = None
    campaign_ids: str | None = None
    ad_ids: str | None = None
    limit: int | None = None
    offset: int | None = None

class AdsGetBudget(VKMethod[Any]):
    __api_method__ = 'ads.getBudget'
    account_id: int = ...

class AdsGetCampaigns(VKMethod[Any]):
    __api_method__ = 'ads.getCampaigns'
    account_id: int = ...
    client_id: int | None = None
    include_deleted: bool | None = None
    campaign_ids: str | None = None
    fields: list[Any] | None = None

class AdsGetCategories(VKMethod[Any]):
    __api_method__ = 'ads.getCategories'
    lang: str | None = None

class AdsGetClients(VKMethod[Any]):
    __api_method__ = 'ads.getClients'
    account_id: int = ...

class AdsGetDemographics(VKMethod[Any]):
    __api_method__ = 'ads.getDemographics'
    account_id: int = ...
    ids_type: str = ...
    ids: str = ...
    period: str = ...
    date_from: str = ...
    date_to: str = ...

class AdsGetFloodStats(VKMethod[Any]):
    __api_method__ = 'ads.getFloodStats'
    account_id: int = ...

class AdsGetLookalikeRequests(VKMethod[Any]):
    __api_method__ = 'ads.getLookalikeRequests'
    account_id: int = ...
    client_id: int | None = None
    requests_ids: str | None = None
    offset: int | None = None
    limit: int | None = None
    sort_by: str | None = None

class AdsGetMusicians(VKMethod[Any]):
    __api_method__ = 'ads.getMusicians'
    artist_name: str = ...

class AdsGetMusiciansByIds(VKMethod[Any]):
    __api_method__ = 'ads.getMusiciansByIds'
    ids: list[Any] = ...

class AdsGetOfficeUsers(VKMethod[Any]):
    __api_method__ = 'ads.getOfficeUsers'
    account_id: int = ...

class AdsGetPostsReach(VKMethod[Any]):
    __api_method__ = 'ads.getPostsReach'
    account_id: int = ...
    ids_type: str = ...
    ids: str = ...

class AdsGetRejectionReason(VKMethod[Any]):
    __api_method__ = 'ads.getRejectionReason'
    account_id: int = ...
    ad_id: int = ...

class AdsGetStatistics(VKMethod[Any]):
    __api_method__ = 'ads.getStatistics'
    account_id: int = ...
    ids_type: str = ...
    ids: str = ...
    period: str = ...
    date_from: str = ...
    date_to: str = ...
    stats_fields: list[Any] | None = None

class AdsGetSuggestions(VKMethod[Any]):
    __api_method__ = 'ads.getSuggestions'
    section: str = ...
    ids: str | None = None
    q: str | None = None
    country: int | None = None
    cities: str | None = None
    lang: str | None = None

class AdsGetTargetGroups(VKMethod[Any]):
    __api_method__ = 'ads.getTargetGroups'
    account_id: int = ...
    client_id: int | None = None
    extended: bool | None = None

class AdsGetTargetPixels(VKMethod[Any]):
    __api_method__ = 'ads.getTargetPixels'
    account_id: int = ...
    client_id: int | None = None

class AdsGetTargetingStats(VKMethod[Any]):
    __api_method__ = 'ads.getTargetingStats'
    account_id: int = ...
    client_id: int | None = None
    criteria: str | None = None
    ad_id: int | None = None
    ad_format: int | None = None
    ad_platform: str | None = None
    ad_platform_no_wall: str | None = None
    ad_platform_no_ad_network: str | None = None
    publisher_platforms: str | None = None
    link_url: str = ...
    link_domain: str | None = None
    need_precise: bool | None = None
    impressions_limit_period: int | None = None

class AdsGetUploadURL(VKMethod[Any]):
    __api_method__ = 'ads.getUploadURL'
    ad_format: int = ...
    icon: int | None = None

class AdsGetVideoUploadURL(VKMethod[Any]):
    __api_method__ = 'ads.getVideoUploadURL'
    pass

class AdsImportTargetContacts(VKMethod[Any]):
    __api_method__ = 'ads.importTargetContacts'
    account_id: int = ...
    client_id: int | None = None
    target_group_id: int = ...
    contacts: str = ...

class AdsRemoveOfficeUsers(VKMethod[Any]):
    __api_method__ = 'ads.removeOfficeUsers'
    account_id: int = ...
    ids: str = ...

class AdsRemoveTargetContacts(VKMethod[Any]):
    __api_method__ = 'ads.removeTargetContacts'
    account_id: int = ...
    client_id: int | None = None
    target_group_id: int = ...
    contacts: str = ...

class AdsSaveLookalikeRequestResult(VKMethod[Any]):
    __api_method__ = 'ads.saveLookalikeRequestResult'
    account_id: int = ...
    client_id: int | None = None
    request_id: int = ...
    level: int = ...

class AdsShareTargetGroup(VKMethod[Any]):
    __api_method__ = 'ads.shareTargetGroup'
    account_id: int = ...
    client_id: int | None = None
    target_group_id: int = ...
    share_with_client_id: int | None = None

class AdsUpdateAds(VKMethod[Any]):
    __api_method__ = 'ads.updateAds'
    account_id: int = ...
    data: str = ...

class AdsUpdateCampaigns(VKMethod[Any]):
    __api_method__ = 'ads.updateCampaigns'
    account_id: int = ...
    data: str = ...

class AdsUpdateClients(VKMethod[Any]):
    __api_method__ = 'ads.updateClients'
    account_id: int = ...
    data: str = ...

class AdsUpdateOfficeUsers(VKMethod[Any]):
    __api_method__ = 'ads.updateOfficeUsers'
    account_id: int = ...
    data: str = ...

class AdsUpdateTargetGroup(VKMethod[Any]):
    __api_method__ = 'ads.updateTargetGroup'
    account_id: int = ...
    client_id: int | None = None
    target_group_id: int = ...
    name: str = ...
    domain: str | None = None
    lifetime: int = ...
    target_pixel_id: int | None = None
    target_pixel_rules: str | None = None

class AdsUpdateTargetPixel(VKMethod[Any]):
    __api_method__ = 'ads.updateTargetPixel'
    account_id: int = ...
    client_id: int | None = None
    target_pixel_id: int = ...
    name: str = ...
    domain: str | None = None
    category_id: int = ...

class AppWidgetsGetAppImageUploadServer(VKMethod[Any]):
    __api_method__ = 'appWidgets.getAppImageUploadServer'
    image_type: str = ...

class AppWidgetsGetAppImages(VKMethod[Any]):
    __api_method__ = 'appWidgets.getAppImages'
    offset: int | None = None
    count: int | None = None
    image_type: str | None = None

class AppWidgetsGetGroupImageUploadServer(VKMethod[Any]):
    __api_method__ = 'appWidgets.getGroupImageUploadServer'
    image_type: str = ...

class AppWidgetsGetGroupImages(VKMethod[Any]):
    __api_method__ = 'appWidgets.getGroupImages'
    offset: int | None = None
    count: int | None = None
    image_type: str | None = None

class AppWidgetsGetImagesById(VKMethod[Any]):
    __api_method__ = 'appWidgets.getImagesById'
    images: list[Any] = ...

class AppWidgetsSaveAppImage(VKMethod[Any]):
    __api_method__ = 'appWidgets.saveAppImage'
    hash: str = ...
    image: str = ...

class AppWidgetsSaveGroupImage(VKMethod[Any]):
    __api_method__ = 'appWidgets.saveGroupImage'
    hash: str = ...
    image: str = ...

class AppWidgetsUpdate(VKMethod[Any]):
    __api_method__ = 'appWidgets.update'
    code: str = ...
    type: str = ...

class AppsAddSnippet(VKMethod[Any]):
    __api_method__ = 'apps.addSnippet'
    vk_ref: list[Any] | None = None
    group_id: list[Any] | None = None
    hash: list[Any] | None = None
    snippet_id: int | None = None
    title: str | None = None
    description: str | None = None
    image_url: str | None = None
    small_image_url: str | None = None
    button: str | None = None

class AppsAddUsersToTestingGroup(VKMethod[Any]):
    __api_method__ = 'apps.addUsersToTestingGroup'
    user_ids: list[Any] = ...
    group_id: int = ...

class AppsDeleteAppRequests(VKMethod[Any]):
    __api_method__ = 'apps.deleteAppRequests'
    pass

class AppsDeleteSnippet(VKMethod[Any]):
    __api_method__ = 'apps.deleteSnippet'
    id: int | None = None

class AppsGet(VKMethod[Any]):
    __api_method__ = 'apps.get'
    app_id: int | None = None
    app_ids: list[Any] | None = None
    platform: str | None = None
    extended: bool | None = None
    return_friends: bool | None = None
    fields: list[Any] | None = None
    name_case: str | None = None
    app_fields: list[Any] | None = None

class AppsGetCatalog(VKMethod[Any]):
    __api_method__ = 'apps.getCatalog'
    sort: str | None = None
    offset: int | None = None
    count: int | None = None
    platform: str | None = None
    extended: bool | None = None
    return_friends: bool | None = None
    fields: list[Any] | None = None
    name_case: str | None = None
    q: str | None = None
    genre_id: int | None = None
    filter: str | None = None

class AppsGetFriendsList(VKMethod[Any]):
    __api_method__ = 'apps.getFriendsList'
    extended: bool | None = None
    count: int | None = None
    offset: int | None = None
    type: str | None = None
    fields: list[Any] | None = None
    query: str | None = None

class AppsGetLeaderboard(VKMethod[Any]):
    __api_method__ = 'apps.getLeaderboard'
    type: str = ...
    global_: bool | None = Field(default=None, alias='global')
    extended: bool | None = None

class AppsGetMiniAppPolicies(VKMethod[Any]):
    __api_method__ = 'apps.getMiniAppPolicies'
    app_id: int = ...

class AppsGetScopes(VKMethod[Any]):
    __api_method__ = 'apps.getScopes'
    type: str | None = None

class AppsGetScore(VKMethod[Any]):
    __api_method__ = 'apps.getScore'
    user_id: int | None = None

class AppsGetSnippets(VKMethod[Any]):
    __api_method__ = 'apps.getSnippets'
    pass

class AppsGetTestingGroups(VKMethod[Any]):
    __api_method__ = 'apps.getTestingGroups'
    group_id: int | None = None

class AppsIsNotificationsAllowed(VKMethod[Any]):
    __api_method__ = 'apps.isNotificationsAllowed'
    user_id: int | None = None

class AppsPromoHasActiveGift(VKMethod[Any]):
    __api_method__ = 'apps.promoHasActiveGift'
    promo_id: int = ...
    user_id: int | None = None

class AppsPromoUseGift(VKMethod[Any]):
    __api_method__ = 'apps.promoUseGift'
    promo_id: int = ...
    user_id: int | None = None

class AppsRemoveTestingGroup(VKMethod[Any]):
    __api_method__ = 'apps.removeTestingGroup'
    group_id: int = ...

class AppsRemoveUsersFromTestingGroups(VKMethod[Any]):
    __api_method__ = 'apps.removeUsersFromTestingGroups'
    user_ids: list[Any] = ...

class AppsSendRequest(VKMethod[Any]):
    __api_method__ = 'apps.sendRequest'
    user_id: int = ...
    text: str | None = None
    type: str | None = None
    name: str | None = None
    key: str | None = None
    separate: bool | None = None

class AppsUpdateMetaForTestingGroup(VKMethod[Any]):
    __api_method__ = 'apps.updateMetaForTestingGroup'
    group_id: int | None = None
    webview: str = ...
    name: str = ...
    platforms: list[Any] = ...
    user_ids: list[Any] | None = None

class AuthRestore(VKMethod[Any]):
    __api_method__ = 'auth.restore'
    phone: str = ...
    last_name: str = ...

class BoardAddTopic(VKMethod[Any]):
    __api_method__ = 'board.addTopic'
    group_id: int = ...
    title: str = ...
    text: str | None = None
    from_group: bool | None = None
    attachments: list[Any] | None = None

class BoardCloseTopic(VKMethod[Any]):
    __api_method__ = 'board.closeTopic'
    group_id: int = ...
    topic_id: int = ...

class BoardCreateComment(VKMethod[Any]):
    __api_method__ = 'board.createComment'
    group_id: int = ...
    topic_id: int = ...
    message: str | None = None
    attachments: list[Any] | None = None
    from_group: bool | None = None
    sticker_id: int | None = None
    guid: str | None = None

class BoardDeleteComment(VKMethod[Any]):
    __api_method__ = 'board.deleteComment'
    group_id: int = ...
    topic_id: int = ...
    comment_id: int = ...

class BoardDeleteTopic(VKMethod[Any]):
    __api_method__ = 'board.deleteTopic'
    group_id: int = ...
    topic_id: int = ...

class BoardEditComment(VKMethod[Any]):
    __api_method__ = 'board.editComment'
    group_id: int = ...
    topic_id: int = ...
    comment_id: int = ...
    message: str | None = None
    attachments: list[Any] | None = None

class BoardEditTopic(VKMethod[Any]):
    __api_method__ = 'board.editTopic'
    group_id: int = ...
    topic_id: int = ...
    title: str = ...

class BoardFixTopic(VKMethod[Any]):
    __api_method__ = 'board.fixTopic'
    group_id: int = ...
    topic_id: int = ...

class BoardGetComments(VKMethod[Any]):
    __api_method__ = 'board.getComments'
    group_id: int = ...
    topic_id: int = ...
    need_likes: bool | None = None
    start_comment_id: int | None = None
    offset: int | None = None
    count: int | None = None
    extended: bool | None = None
    sort: str | None = None

class BoardGetTopics(VKMethod[Any]):
    __api_method__ = 'board.getTopics'
    group_id: int = ...
    topic_ids: list[Any] | None = None
    order: int | None = None
    offset: int | None = None
    count: int | None = None
    extended: bool | None = None
    preview: int | None = None
    preview_length: int | None = None

class BoardOpenTopic(VKMethod[Any]):
    __api_method__ = 'board.openTopic'
    group_id: int = ...
    topic_id: int = ...

class BoardRestoreComment(VKMethod[Any]):
    __api_method__ = 'board.restoreComment'
    group_id: int = ...
    topic_id: int = ...
    comment_id: int = ...

class BoardUnfixTopic(VKMethod[Any]):
    __api_method__ = 'board.unfixTopic'
    group_id: int = ...
    topic_id: int = ...

class BugtrackerAddCompanyGroupsMembers(VKMethod[Any]):
    __api_method__ = 'bugtracker.addCompanyGroupsMembers'
    company_id: int = ...
    user_ids: list[Any] = ...
    company_group_ids: list[Any] = ...

class BugtrackerAddCompanyMembers(VKMethod[Any]):
    __api_method__ = 'bugtracker.addCompanyMembers'
    user_ids: list[Any] = ...
    company_id: int = ...

class BugtrackerChangeBugreportStatus(VKMethod[Any]):
    __api_method__ = 'bugtracker.changeBugreportStatus'
    bugreport_id: int = ...
    status: int | None = None
    comment: str | None = None
    from_statuses: list[Any] | None = None
    not_in_statuses: list[Any] | None = None

class BugtrackerCreateComment(VKMethod[Any]):
    __api_method__ = 'bugtracker.createComment'
    bugreport_id: int = ...
    text: str | None = None
    hidden: bool | None = None
    hidden_attachments: bool | None = None
    force: bool | None = None

class BugtrackerGetBugreportById(VKMethod[Any]):
    __api_method__ = 'bugtracker.getBugreportById'
    bugreport_id: int = ...
    extended: bool | None = None
    fields: list[Any] | None = None

class BugtrackerGetCompanyGroupMembers(VKMethod[Any]):
    __api_method__ = 'bugtracker.getCompanyGroupMembers'
    company_id: int = ...
    company_group_id: int = ...
    count: int | None = None
    offset: int | None = None
    filter_name: str | None = None
    extended: bool | None = None
    fields: list[Any] | None = None

class BugtrackerGetCompanyMembers(VKMethod[Any]):
    __api_method__ = 'bugtracker.getCompanyMembers'
    company_id: int = ...
    count: int | None = None
    offset: int | None = None
    filter_name: str | None = None
    filter_role: int | None = None
    filter_not_group: int | None = None
    filter_member_ids: list[Any] | None = None
    extended: bool | None = None
    fields: list[Any] | None = None
    extra: bool | None = None

class BugtrackerGetDownloadVersionUrl(VKMethod[Any]):
    __api_method__ = 'bugtracker.getDownloadVersionUrl'
    product_id: int = ...
    version_id: int = ...
    ttl: int | None = None

class BugtrackerGetProductBuildUploadServer(VKMethod[Any]):
    __api_method__ = 'bugtracker.getProductBuildUploadServer'
    product_id: int = ...

class BugtrackerRemoveCompanyGroupMember(VKMethod[Any]):
    __api_method__ = 'bugtracker.removeCompanyGroupMember'
    company_id: int = ...
    user_id: int = ...
    company_group_id: int = ...

class BugtrackerRemoveCompanyMember(VKMethod[Any]):
    __api_method__ = 'bugtracker.removeCompanyMember'
    user_id: int = ...
    company_id: int = ...

class BugtrackerSaveProductVersion(VKMethod[Any]):
    __api_method__ = 'bugtracker.saveProductVersion'
    product_id: int | None = None
    version_id: int | None = None
    title: str = ...
    release_notes: str | None = None
    visible: bool | None = None
    set_rft: bool | None = None

class BugtrackerSetCompanyMemberRole(VKMethod[Any]):
    __api_method__ = 'bugtracker.setCompanyMemberRole'
    user_id: int = ...
    company_id: int = ...
    role: int = ...

class BugtrackerSetProductIsOver(VKMethod[Any]):
    __api_method__ = 'bugtracker.setProductIsOver'
    product_id: int = ...
    is_over: bool | None = None

class CallsForceFinish(VKMethod[Any]):
    __api_method__ = 'calls.forceFinish'
    call_id: str = ...

class CallsStart(VKMethod[Any]):
    __api_method__ = 'calls.start'
    group_id: int | None = None

class DatabaseGetChairs(VKMethod[Any]):
    __api_method__ = 'database.getChairs'
    faculty_id: int = ...
    offset: int | None = None
    count: int | None = None

class DatabaseGetCities(VKMethod[Any]):
    __api_method__ = 'database.getCities'
    region_id: int | None = None
    q: str | None = None
    need_all: bool | None = None
    offset: int | None = None
    count: int | None = None
    fields: list[Any] | None = None

class DatabaseGetCitiesById(VKMethod[Any]):
    __api_method__ = 'database.getCitiesById'
    city_ids: list[Any] | None = None
    fields: list[Any] | None = None

class DatabaseGetCountries(VKMethod[Any]):
    __api_method__ = 'database.getCountries'
    need_all: bool | None = None
    code: str | None = None
    offset: int | None = None
    count: int | None = None

class DatabaseGetCountriesById(VKMethod[Any]):
    __api_method__ = 'database.getCountriesById'
    country_ids: list[Any] | None = None

class DatabaseGetFaculties(VKMethod[Any]):
    __api_method__ = 'database.getFaculties'
    university_id: int = ...
    offset: int | None = None
    count: int | None = None

class DatabaseGetMetroStations(VKMethod[Any]):
    __api_method__ = 'database.getMetroStations'
    city_id: int = ...
    offset: int | None = None
    count: int | None = None
    extended: bool | None = None

class DatabaseGetMetroStationsById(VKMethod[Any]):
    __api_method__ = 'database.getMetroStationsById'
    station_ids: list[Any] | None = None

class DatabaseGetRegions(VKMethod[Any]):
    __api_method__ = 'database.getRegions'
    q: str | None = None
    offset: int | None = None
    count: int | None = None

class DatabaseGetSchoolClasses(VKMethod[Any]):
    __api_method__ = 'database.getSchoolClasses'
    country_id: int | None = None

class DatabaseGetSchools(VKMethod[Any]):
    __api_method__ = 'database.getSchools'
    q: str | None = None
    city_id: int = ...
    offset: int | None = None
    count: int | None = None

class DatabaseGetUniversities(VKMethod[Any]):
    __api_method__ = 'database.getUniversities'
    q: str | None = None
    city_id: int | None = None
    offset: int | None = None
    count: int | None = None

class DocsAdd(VKMethod[Any]):
    __api_method__ = 'docs.add'
    owner_id: int = ...
    doc_id: int = ...
    access_key: str | None = None

class DocsDelete(VKMethod[Any]):
    __api_method__ = 'docs.delete'
    owner_id: int = ...
    doc_id: int = ...

class DocsEdit(VKMethod[Any]):
    __api_method__ = 'docs.edit'
    owner_id: int | None = None
    doc_id: int = ...
    title: str = ...
    tags: list[Any] | None = None

class DocsGet(VKMethod[Any]):
    __api_method__ = 'docs.get'
    count: int | None = None
    offset: int | None = None
    type: int | None = None
    owner_id: int | None = None
    return_tags: bool | None = None

class DocsGetById(VKMethod[Any]):
    __api_method__ = 'docs.getById'
    docs: list[Any] = ...
    return_tags: bool | None = None

class DocsGetMessagesUploadServer(VKMethod[Any]):
    __api_method__ = 'docs.getMessagesUploadServer'
    type: str | None = None
    peer_id: int | None = None

class DocsGetTypes(VKMethod[Any]):
    __api_method__ = 'docs.getTypes'
    owner_id: int | None = None

class DocsGetUploadServer(VKMethod[Any]):
    __api_method__ = 'docs.getUploadServer'
    group_id: int | None = None

class DocsGetWallUploadServer(VKMethod[Any]):
    __api_method__ = 'docs.getWallUploadServer'
    group_id: int | None = None

class DocsRestore(VKMethod[Any]):
    __api_method__ = 'docs.restore'
    owner_id: int = ...
    doc_id: int = ...

class DocsSave(VKMethod[Any]):
    __api_method__ = 'docs.save'
    file: str = ...
    title: str | None = None
    tags: str | None = None
    return_tags: bool | None = None

class DocsSearch(VKMethod[Any]):
    __api_method__ = 'docs.search'
    q: str | None = None
    search_own: bool | None = None
    count: int | None = None
    offset: int | None = None
    return_tags: bool | None = None

class DonutGetFriends(VKMethod[Any]):
    __api_method__ = 'donut.getFriends'
    owner_id: int = ...
    offset: int | None = None
    count: int | None = None
    fields: list[Any] | None = None

class DonutGetSubscription(VKMethod[Any]):
    __api_method__ = 'donut.getSubscription'
    owner_id: int = ...

class DonutGetSubscriptions(VKMethod[Any]):
    __api_method__ = 'donut.getSubscriptions'
    fields: list[Any] | None = None
    offset: int | None = None
    count: int | None = None

class DonutIsDon(VKMethod[Any]):
    __api_method__ = 'donut.isDon'
    owner_id: int = ...

class DownloadedGamesGetPaidStatus(VKMethod[Any]):
    __api_method__ = 'downloadedGames.getPaidStatus'
    user_id: int | None = None

class Execute(VKMethod[Any]):
    __api_method__ = 'execute'
    pass

class FaveAddArticle(VKMethod[Any]):
    __api_method__ = 'fave.addArticle'
    url: str = ...

class FaveAddLink(VKMethod[Any]):
    __api_method__ = 'fave.addLink'
    link: str = ...

class FaveAddPage(VKMethod[Any]):
    __api_method__ = 'fave.addPage'
    user_id: int | None = None
    group_id: int | None = None

class FaveAddPost(VKMethod[Any]):
    __api_method__ = 'fave.addPost'
    owner_id: int = ...
    id: int = ...
    access_key: str | None = None

class FaveAddProduct(VKMethod[Any]):
    __api_method__ = 'fave.addProduct'
    owner_id: int = ...
    id: int = ...
    access_key: str | None = None

class FaveAddTag(VKMethod[Any]):
    __api_method__ = 'fave.addTag'
    name: str | None = None
    position: str | None = None

class FaveAddVideo(VKMethod[Any]):
    __api_method__ = 'fave.addVideo'
    owner_id: int = ...
    id: int = ...
    access_key: str | None = None

class FaveEditTag(VKMethod[Any]):
    __api_method__ = 'fave.editTag'
    id: int = ...
    name: str = ...

class FaveGet(VKMethod[Any]):
    __api_method__ = 'fave.get'
    extended: bool | None = None
    item_type: str | None = None
    tag_id: int | None = None
    offset: int | None = None
    count: int | None = None
    fields: str | None = None
    is_from_snackbar: bool | None = None

class FaveGetPages(VKMethod[Any]):
    __api_method__ = 'fave.getPages'
    offset: int | None = None
    count: int | None = None
    type: str | None = None
    fields: list[Any] | None = None
    tag_id: int | None = None

class FaveGetTags(VKMethod[Any]):
    __api_method__ = 'fave.getTags'
    pass

class FaveMarkSeen(VKMethod[Any]):
    __api_method__ = 'fave.markSeen'
    pass

class FaveRemoveArticle(VKMethod[Any]):
    __api_method__ = 'fave.removeArticle'
    owner_id: int = ...
    article_id: int = ...

class FaveRemoveLink(VKMethod[Any]):
    __api_method__ = 'fave.removeLink'
    link_id: str | None = None
    link: str | None = None

class FaveRemovePage(VKMethod[Any]):
    __api_method__ = 'fave.removePage'
    user_id: int | None = None
    group_id: int | None = None

class FaveRemovePost(VKMethod[Any]):
    __api_method__ = 'fave.removePost'
    owner_id: int = ...
    id: int = ...

class FaveRemoveProduct(VKMethod[Any]):
    __api_method__ = 'fave.removeProduct'
    owner_id: int = ...
    id: int = ...

class FaveRemoveTag(VKMethod[Any]):
    __api_method__ = 'fave.removeTag'
    id: int = ...

class FaveRemoveVideo(VKMethod[Any]):
    __api_method__ = 'fave.removeVideo'
    owner_id: int = ...
    id: int = ...

class FaveReorderTags(VKMethod[Any]):
    __api_method__ = 'fave.reorderTags'
    ids: list[Any] = ...

class FaveSetPageTags(VKMethod[Any]):
    __api_method__ = 'fave.setPageTags'
    user_id: int | None = None
    group_id: int | None = None
    tag_ids: list[Any] | None = None

class FaveSetTags(VKMethod[Any]):
    __api_method__ = 'fave.setTags'
    item_type: str | None = None
    item_owner_id: int | None = None
    item_id: int | None = None
    tag_ids: list[Any] | None = None
    link_id: str | None = None
    link_url: str | None = None

class FaveTrackPageInteraction(VKMethod[Any]):
    __api_method__ = 'fave.trackPageInteraction'
    user_id: int | None = None
    group_id: int | None = None

class FriendsAdd(VKMethod[Any]):
    __api_method__ = 'friends.add'
    user_id: int | None = None
    text: str | None = None
    follow: bool | None = None

class FriendsAddList(VKMethod[Any]):
    __api_method__ = 'friends.addList'
    name: str = ...
    user_ids: list[Any] | None = None

class FriendsAreFriends(VKMethod[Any]):
    __api_method__ = 'friends.areFriends'
    user_ids: list[Any] = ...
    need_sign: bool | None = None
    extended: bool | None = None

class FriendsDelete(VKMethod[Any]):
    __api_method__ = 'friends.delete'
    user_id: int | None = None

class FriendsDeleteAllRequests(VKMethod[Any]):
    __api_method__ = 'friends.deleteAllRequests'
    pass

class FriendsDeleteList(VKMethod[Any]):
    __api_method__ = 'friends.deleteList'
    list_id: int = ...

class FriendsEdit(VKMethod[Any]):
    __api_method__ = 'friends.edit'
    user_id: int = ...
    list_ids: list[Any] | None = None

class FriendsEditList(VKMethod[Any]):
    __api_method__ = 'friends.editList'
    name: str | None = None
    list_id: int = ...
    user_ids: list[Any] | None = None
    add_user_ids: list[Any] | None = None
    delete_user_ids: list[Any] | None = None

class FriendsGet(VKMethod[Any]):
    __api_method__ = 'friends.get'
    user_id: int | None = None
    order: str | None = None
    list_id: int | None = None
    count: int | None = None
    offset: int | None = None
    fields: list[Any] | None = None
    ref: str | None = None

class FriendsGetAppUsers(VKMethod[Any]):
    __api_method__ = 'friends.getAppUsers'
    pass

class FriendsGetLists(VKMethod[Any]):
    __api_method__ = 'friends.getLists'
    user_id: int | None = None
    return_system: bool | None = None

class FriendsGetMutual(VKMethod[Any]):
    __api_method__ = 'friends.getMutual'
    source_uid: int | None = None
    target_uid: int | None = None
    target_uids: list[Any] | None = None
    order: str | None = None
    count: int | None = None
    offset: int | None = None
    need_common_count: bool | None = None

class FriendsGetOnline(VKMethod[Any]):
    __api_method__ = 'friends.getOnline'
    user_id: int | None = None
    list_id: int | None = None
    online_mobile: bool | None = None
    order: str | None = None
    count: int | None = None
    offset: int | None = None

class FriendsGetRecent(VKMethod[Any]):
    __api_method__ = 'friends.getRecent'
    count: int | None = None

class FriendsGetRequests(VKMethod[Any]):
    __api_method__ = 'friends.getRequests'
    offset: int | None = None
    count: int | None = None
    extended: bool | None = None
    need_mutual: bool | None = None
    out: bool | None = None
    sort: int | None = None
    need_viewed: bool | None = None
    suggested: bool | None = None
    ref: str | None = None
    fields: list[Any] | None = None

class FriendsGetSuggestions(VKMethod[Any]):
    __api_method__ = 'friends.getSuggestions'
    filter: list[Any] | None = None
    count: int | None = None
    offset: int | None = None
    fields: list[Any] | None = None
    name_case: str | None = None

class FriendsSearch(VKMethod[Any]):
    __api_method__ = 'friends.search'
    user_id: int | None = None
    q: str | None = None
    fields: list[Any] | None = None
    name_case: str | None = None
    offset: int | None = None
    count: int | None = None

class GiftsGet(VKMethod[Any]):
    __api_method__ = 'gifts.get'
    user_id: int | None = None
    count: int | None = None
    offset: int | None = None

class GroupsAddAddress(VKMethod[Any]):
    __api_method__ = 'groups.addAddress'
    group_id: int = ...
    title: str = ...
    address: str = ...
    additional_address: str | None = None
    city_id: int = ...
    metro_id: int | None = None
    latitude: float = ...
    longitude: float = ...
    phone: str | None = None
    work_info_status: str | None = None
    timetable: str | None = None
    is_main_address: bool | None = None

class GroupsAddCallbackServer(VKMethod[Any]):
    __api_method__ = 'groups.addCallbackServer'
    group_id: int = ...
    url: str = ...
    title: str = ...
    secret_key: str | None = None

class GroupsAddLink(VKMethod[Any]):
    __api_method__ = 'groups.addLink'
    group_id: int = ...
    link: str = ...
    text: str | None = None

class GroupsApproveRequest(VKMethod[Any]):
    __api_method__ = 'groups.approveRequest'
    group_id: int = ...
    user_id: int = ...

class GroupsBan(VKMethod[Any]):
    __api_method__ = 'groups.ban'
    group_id: int = ...
    owner_id: int | None = None
    end_date: int | None = None
    reason: int | None = None
    comment: str | None = None
    comment_visible: bool | None = None

class GroupsCreate(VKMethod[Any]):
    __api_method__ = 'groups.create'
    title: str = ...
    description: str | None = None
    type: str | None = None
    public_category: int | None = None
    public_subcategory: int | None = None
    subtype: int | None = None

class GroupsDeleteAddress(VKMethod[Any]):
    __api_method__ = 'groups.deleteAddress'
    group_id: int = ...
    address_id: int = ...

class GroupsDeleteCallbackServer(VKMethod[Any]):
    __api_method__ = 'groups.deleteCallbackServer'
    group_id: int = ...
    server_id: int = ...

class GroupsDeleteLink(VKMethod[Any]):
    __api_method__ = 'groups.deleteLink'
    group_id: int = ...
    link_id: int = ...

class GroupsDisableOnline(VKMethod[Any]):
    __api_method__ = 'groups.disableOnline'
    group_id: int = ...

class GroupsEdit(VKMethod[Any]):
    __api_method__ = 'groups.edit'
    group_id: int = ...
    title: str | None = None
    description: str | None = None
    screen_name: str | None = None
    access: int | None = None
    website: str | None = None
    subject: int | None = None
    email: str | None = None
    phone: str | None = None
    rss: str | None = None
    event_start_date: int | None = None
    event_finish_date: int | None = None
    event_group_id: int | None = None
    public_category: int | None = None
    public_subcategory: int | None = None
    public_date: str | None = None
    wall: int | None = None
    topics: int | None = None
    photos: int | None = None
    video: int | None = None
    audio: int | None = None
    links: bool | None = None
    events: bool | None = None
    places: bool | None = None
    contacts: bool | None = None
    docs: int | None = None
    wiki: int | None = None
    messages: bool | None = None
    articles: bool | None = None
    addresses: bool | None = None
    age_limits: int | None = None
    market: bool | None = None
    market_buttons: str | None = None
    market_comments: bool | None = None
    market_country: list[Any] | None = None
    market_city: list[Any] | None = None
    market_currency: int | None = None
    market_contact: int | None = None
    market_wiki: int | None = None
    obscene_filter: bool | None = None
    obscene_stopwords: bool | None = None
    toxic_filter: bool | None = None
    disable_replies_from_groups: bool | None = None
    obscene_words: list[Any] | None = None
    main_section: int | None = None
    secondary_section: int | None = None
    country: int | None = None
    city: int | None = None

class GroupsEditAddress(VKMethod[Any]):
    __api_method__ = 'groups.editAddress'
    group_id: int = ...
    address_id: int = ...
    title: str | None = None
    address: str | None = None
    additional_address: str | None = None
    city_id: int | None = None
    metro_id: int | None = None
    latitude: float | None = None
    longitude: float | None = None
    phone: str | None = None
    work_info_status: str | None = None
    timetable: str | None = None
    is_main_address: bool | None = None

class GroupsEditCallbackServer(VKMethod[Any]):
    __api_method__ = 'groups.editCallbackServer'
    group_id: int = ...
    server_id: int = ...
    url: str = ...
    title: str = ...
    secret_key: str | None = None

class GroupsEditLink(VKMethod[Any]):
    __api_method__ = 'groups.editLink'
    group_id: int = ...
    link_id: int = ...
    text: str | None = None

class GroupsEditManager(VKMethod[Any]):
    __api_method__ = 'groups.editManager'
    group_id: int = ...
    user_id: int = ...
    role: str | None = None
    is_call_operator: bool | None = None
    is_contact: bool | None = None
    contact_position: str | None = None
    contact_phone: str | None = None
    contact_email: str | None = None

class GroupsEnableOnline(VKMethod[Any]):
    __api_method__ = 'groups.enableOnline'
    group_id: int = ...

class GroupsGet(VKMethod[Any]):
    __api_method__ = 'groups.get'
    user_id: int | None = None
    extended: bool | None = None
    filter: list[Any] | None = None
    fields: list[Any] | None = None
    offset: int | None = None
    count: int | None = None

class GroupsGetAddresses(VKMethod[Any]):
    __api_method__ = 'groups.getAddresses'
    group_id: int = ...
    address_ids: list[Any] | None = None
    latitude: float | None = None
    longitude: float | None = None
    offset: int | None = None
    count: int | None = None
    fields: list[Any] | None = None

class GroupsGetBanned(VKMethod[Any]):
    __api_method__ = 'groups.getBanned'
    group_id: int = ...
    offset: int | None = None
    count: int | None = None
    fields: list[Any] | None = None
    owner_id: int | None = None

class GroupsGetById(VKMethod[Any]):
    __api_method__ = 'groups.getById'
    group_ids: list[Any] | None = None
    group_id: int | str | None = None
    fields: list[Any] | None = None

class GroupsGetCallbackConfirmationCode(VKMethod[Any]):
    __api_method__ = 'groups.getCallbackConfirmationCode'
    group_id: int = ...

class GroupsGetCallbackServers(VKMethod[Any]):
    __api_method__ = 'groups.getCallbackServers'
    group_id: int = ...
    server_ids: list[Any] | None = None

class GroupsGetCallbackSettings(VKMethod[Any]):
    __api_method__ = 'groups.getCallbackSettings'
    group_id: int = ...
    server_id: int | None = None

class GroupsGetCatalogInfo(VKMethod[Any]):
    __api_method__ = 'groups.getCatalogInfo'
    extended: bool | None = None
    subcategories: bool | None = None

class GroupsGetInvitedUsers(VKMethod[Any]):
    __api_method__ = 'groups.getInvitedUsers'
    group_id: int = ...
    offset: int | None = None
    count: int | None = None
    fields: list[Any] | None = None
    name_case: str | None = None

class GroupsGetInvites(VKMethod[Any]):
    __api_method__ = 'groups.getInvites'
    offset: int | None = None
    count: int | None = None
    extended: bool | None = None

class GroupsGetLongPollServer(VKMethod[Any]):
    __api_method__ = 'groups.getLongPollServer'
    group_id: int = ...

class GroupsGetLongPollSettings(VKMethod[Any]):
    __api_method__ = 'groups.getLongPollSettings'
    group_id: int = ...

class GroupsGetMembers(VKMethod[Any]):
    __api_method__ = 'groups.getMembers'
    group_id: int | str | None = None
    sort: str | None = None
    offset: int | None = None
    count: int | None = None
    fields: list[Any] | None = None
    filter: str | None = None

class GroupsGetOnlineStatus(VKMethod[Any]):
    __api_method__ = 'groups.getOnlineStatus'
    group_id: int = ...

class GroupsGetRequests(VKMethod[Any]):
    __api_method__ = 'groups.getRequests'
    group_id: int = ...
    offset: int | None = None
    count: int | None = None
    fields: list[Any] | None = None

class GroupsGetSettings(VKMethod[Any]):
    __api_method__ = 'groups.getSettings'
    group_id: int | str = ...

class GroupsGetTagList(VKMethod[Any]):
    __api_method__ = 'groups.getTagList'
    group_id: int = ...

class GroupsGetTokenPermissions(VKMethod[Any]):
    __api_method__ = 'groups.getTokenPermissions'
    pass

class GroupsInvite(VKMethod[Any]):
    __api_method__ = 'groups.invite'
    group_id: int = ...
    user_id: int | None = None
    user_ids_list: list[Any] | None = None

class GroupsIsMember(VKMethod[Any]):
    __api_method__ = 'groups.isMember'
    group_id: int | str = ...
    user_id: int | None = None
    user_ids: list[Any] | None = None
    extended: bool | None = None

class GroupsJoin(VKMethod[Any]):
    __api_method__ = 'groups.join'
    group_id: int = ...
    not_sure: str | None = None

class GroupsLeave(VKMethod[Any]):
    __api_method__ = 'groups.leave'
    group_id: int = ...

class GroupsRemoveUser(VKMethod[Any]):
    __api_method__ = 'groups.removeUser'
    group_id: int = ...
    user_id: int = ...

class GroupsReorderLink(VKMethod[Any]):
    __api_method__ = 'groups.reorderLink'
    group_id: int = ...
    link_id: int = ...
    after: int | None = None

class GroupsSearch(VKMethod[Any]):
    __api_method__ = 'groups.search'
    q: str = ...
    type: str | None = None
    country_id: int | None = None
    city_id: int | None = None
    future: bool | None = None
    market: bool | None = None
    sort: int | None = None
    offset: int | None = None
    count: int | None = None

class GroupsSetCallbackSettings(VKMethod[Any]):
    __api_method__ = 'groups.setCallbackSettings'
    group_id: int = ...
    server_id: int | None = None
    api_version: str | None = None
    message_new: bool | None = None
    message_reply: bool | None = None
    message_allow: bool | None = None
    message_edit: bool | None = None
    message_deny: bool | None = None
    message_typing_state: bool | None = None
    message_read: bool | None = None
    photo_new: bool | None = None
    audio_new: bool | None = None
    video_new: bool | None = None
    wall_reply_new: bool | None = None
    wall_reply_edit: bool | None = None
    wall_reply_delete: bool | None = None
    wall_reply_restore: bool | None = None
    wall_post_new: bool | None = None
    wall_repost: bool | None = None
    wall_schedule_post_new: bool | None = None
    wall_schedule_post_delete: bool | None = None
    board_post_new: bool | None = None
    board_post_edit: bool | None = None
    board_post_restore: bool | None = None
    board_post_delete: bool | None = None
    photo_comment_new: bool | None = None
    photo_comment_edit: bool | None = None
    photo_comment_delete: bool | None = None
    photo_comment_restore: bool | None = None
    video_comment_new: bool | None = None
    video_comment_edit: bool | None = None
    video_comment_delete: bool | None = None
    video_comment_restore: bool | None = None
    market_comment_new: bool | None = None
    market_comment_edit: bool | None = None
    market_comment_delete: bool | None = None
    market_comment_restore: bool | None = None
    market_order_new: bool | None = None
    market_order_edit: bool | None = None
    poll_vote_new: bool | None = None
    group_join: bool | None = None
    group_leave: bool | None = None
    group_change_settings: bool | None = None
    group_change_photo: bool | None = None
    group_officers_edit: bool | None = None
    user_block: bool | None = None
    user_unblock: bool | None = None
    lead_forms_new: bool | None = None
    like_add: bool | None = None
    like_remove: bool | None = None
    message_event: bool | None = None
    message_reaction_event: bool | None = None
    donut_subscription_create: bool | None = None
    donut_subscription_prolonged: bool | None = None
    donut_subscription_cancelled: bool | None = None
    donut_subscription_price_changed: bool | None = None
    donut_subscription_expired: bool | None = None
    donut_money_withdraw: bool | None = None
    donut_money_withdraw_error: bool | None = None

class GroupsSetLongPollSettings(VKMethod[Any]):
    __api_method__ = 'groups.setLongPollSettings'
    group_id: int = ...
    enabled: bool | None = None
    api_version: str | None = None
    message_new: bool | None = None
    message_reply: bool | None = None
    message_allow: bool | None = None
    message_deny: bool | None = None
    message_edit: bool | None = None
    message_typing_state: bool | None = None
    message_read: bool | None = None
    photo_new: bool | None = None
    audio_new: bool | None = None
    video_new: bool | None = None
    wall_reply_new: bool | None = None
    wall_reply_edit: bool | None = None
    wall_reply_delete: bool | None = None
    wall_reply_restore: bool | None = None
    wall_post_new: bool | None = None
    wall_repost: bool | None = None
    board_post_new: bool | None = None
    board_post_edit: bool | None = None
    board_post_restore: bool | None = None
    board_post_delete: bool | None = None
    photo_comment_new: bool | None = None
    photo_comment_edit: bool | None = None
    photo_comment_delete: bool | None = None
    photo_comment_restore: bool | None = None
    video_comment_new: bool | None = None
    video_comment_edit: bool | None = None
    video_comment_delete: bool | None = None
    video_comment_restore: bool | None = None
    market_comment_new: bool | None = None
    market_comment_edit: bool | None = None
    market_comment_delete: bool | None = None
    market_comment_restore: bool | None = None
    poll_vote_new: bool | None = None
    group_join: bool | None = None
    group_leave: bool | None = None
    group_change_settings: bool | None = None
    group_change_photo: bool | None = None
    group_officers_edit: bool | None = None
    user_block: bool | None = None
    user_unblock: bool | None = None
    like_add: bool | None = None
    like_remove: bool | None = None
    message_event: bool | None = None
    message_reaction_event: bool | None = None
    donut_subscription_create: bool | None = None
    donut_subscription_prolonged: bool | None = None
    donut_subscription_cancelled: bool | None = None
    donut_subscription_price_changed: bool | None = None
    donut_subscription_expired: bool | None = None
    donut_money_withdraw: bool | None = None
    donut_money_withdraw_error: bool | None = None

class GroupsSetSettings(VKMethod[Any]):
    __api_method__ = 'groups.setSettings'
    group_id: int = ...
    messages: bool | None = None
    bots_capabilities: bool | None = None
    bots_start_button: bool | None = None
    bots_add_to_chat: bool | None = None
    bot_online_booking_enabled: bool | None = None

class GroupsSetUserNote(VKMethod[Any]):
    __api_method__ = 'groups.setUserNote'
    group_id: int = ...
    user_id: int = ...
    note: str | None = None

class GroupsTagAdd(VKMethod[Any]):
    __api_method__ = 'groups.tagAdd'
    group_id: int = ...
    tag_name: str = ...
    tag_color: str | None = None

class GroupsTagBind(VKMethod[Any]):
    __api_method__ = 'groups.tagBind'
    group_id: int = ...
    tag_id: int = ...
    user_id: int = ...
    act: str = ...

class GroupsTagDelete(VKMethod[Any]):
    __api_method__ = 'groups.tagDelete'
    group_id: int = ...
    tag_id: int = ...

class GroupsTagUpdate(VKMethod[Any]):
    __api_method__ = 'groups.tagUpdate'
    group_id: int = ...
    tag_id: int = ...
    tag_name: str = ...

class GroupsToggleMarket(VKMethod[Any]):
    __api_method__ = 'groups.toggleMarket'
    group_id: int = ...
    state: str = ...
    ref: str | None = None

class GroupsUnban(VKMethod[Any]):
    __api_method__ = 'groups.unban'
    group_id: int = ...
    owner_id: int | None = None

class LeadFormsCreate(VKMethod[Any]):
    __api_method__ = 'leadForms.create'
    group_id: int = ...
    name: str = ...
    title: str = ...
    description: str = ...
    questions: str = ...
    policy_link_url: str = ...
    photo: str | None = None
    confirmation: str | None = None
    site_link_url: str | None = None
    active: bool | None = None
    once_per_user: bool | None = None
    pixel_code: str | None = None
    notify_admins: list[Any] | None = None
    notify_emails: list[Any] | None = None

class LeadFormsDelete(VKMethod[Any]):
    __api_method__ = 'leadForms.delete'
    group_id: int = ...
    form_id: int = ...

class LeadFormsGet(VKMethod[Any]):
    __api_method__ = 'leadForms.get'
    group_id: int = ...
    form_id: int = ...

class LeadFormsGetLeads(VKMethod[Any]):
    __api_method__ = 'leadForms.getLeads'
    group_id: int = ...
    form_id: int = ...
    limit: int | None = None
    next_page_token: str | None = None

class LeadFormsGetUploadURL(VKMethod[Any]):
    __api_method__ = 'leadForms.getUploadURL'
    pass

class LeadFormsList(VKMethod[Any]):
    __api_method__ = 'leadForms.list'
    group_id: int = ...

class LeadFormsUpdate(VKMethod[Any]):
    __api_method__ = 'leadForms.update'
    group_id: int = ...
    form_id: int = ...
    name: str = ...
    title: str = ...
    description: str = ...
    questions: str = ...
    policy_link_url: str = ...
    photo: str | None = None
    confirmation: str | None = None
    site_link_url: str | None = None
    active: bool | None = None
    once_per_user: bool | None = None
    pixel_code: str | None = None
    notify_admins: list[Any] | None = None
    notify_emails: list[Any] | None = None

class LikesAdd(VKMethod[Any]):
    __api_method__ = 'likes.add'
    type: str = ...
    owner_id: int | None = None
    item_id: int = ...
    access_key: str | None = None
    from_group: bool | None = None

class LikesDelete(VKMethod[Any]):
    __api_method__ = 'likes.delete'
    type: str = ...
    owner_id: int | None = None
    item_id: int = ...
    access_key: str | None = None
    from_group: bool | None = None

class LikesGetList(VKMethod[Any]):
    __api_method__ = 'likes.getList'
    type: str = ...
    owner_id: int | None = None
    item_id: int | None = None
    page_url: str | None = None
    filter: str | None = None
    friends_only: int | None = None
    extended: bool | None = None
    offset: int | None = None
    count: int | None = None
    skip_own: bool | None = None
    fields: list[Any] | None = None

class LikesIsLiked(VKMethod[Any]):
    __api_method__ = 'likes.isLiked'
    user_id: int | None = None
    type: str = ...
    owner_id: int | None = None
    item_id: int = ...

class MarketAdd(VKMethod[Any]):
    __api_method__ = 'market.add'
    owner_id: int = ...
    name: str = ...
    description: str = ...
    category_id: int = ...
    price: float | None = None
    old_price: float | None = None
    deleted: bool | None = None
    main_photo_id: int | None = None
    photo_ids: list[Any] | None = None
    video_ids: list[Any] | None = None
    url: str | None = None
    variant_ids: list[Any] | None = None
    is_main_variant: bool | None = None
    dimension_width: int | None = None
    dimension_height: int | None = None
    dimension_length: int | None = None
    weight: int | None = None
    sku: str | None = None
    stock_amount: int | None = None

class MarketAddAlbum(VKMethod[Any]):
    __api_method__ = 'market.addAlbum'
    owner_id: int = ...
    title: str = ...
    photo_id: int | None = None
    main_album: bool | None = None
    is_hidden: bool | None = None

class MarketAddProperty(VKMethod[Any]):
    __api_method__ = 'market.addProperty'
    group_id: int = ...
    title: str = ...

class MarketAddPropertyVariant(VKMethod[Any]):
    __api_method__ = 'market.addPropertyVariant'
    group_id: int = ...
    property_id: int = ...
    title: str = ...

class MarketAddToAlbum(VKMethod[Any]):
    __api_method__ = 'market.addToAlbum'
    owner_id: int = ...
    item_ids: list[Any] = ...
    album_ids: list[Any] = ...

class MarketCreateComment(VKMethod[Any]):
    __api_method__ = 'market.createComment'
    owner_id: int = ...
    item_id: int = ...
    message: str | None = None
    attachments: list[Any] | None = None
    from_group: bool | None = None
    reply_to_comment: int | None = None
    sticker_id: int | None = None
    guid: str | None = None

class MarketDelete(VKMethod[Any]):
    __api_method__ = 'market.delete'
    owner_id: int = ...
    item_id: int = ...

class MarketDeleteAlbum(VKMethod[Any]):
    __api_method__ = 'market.deleteAlbum'
    owner_id: int = ...
    album_id: int = ...

class MarketDeleteComment(VKMethod[Any]):
    __api_method__ = 'market.deleteComment'
    owner_id: int = ...
    comment_id: int = ...

class MarketDeleteProperty(VKMethod[Any]):
    __api_method__ = 'market.deleteProperty'
    group_id: int = ...
    property_id: int = ...

class MarketDeletePropertyVariant(VKMethod[Any]):
    __api_method__ = 'market.deletePropertyVariant'
    group_id: int = ...
    variant_id: int = ...

class MarketEdit(VKMethod[Any]):
    __api_method__ = 'market.edit'
    owner_id: int = ...
    item_id: int = ...
    name: str | None = None
    description: str | None = None
    category_id: int | None = None
    price: float | None = None
    old_price: float | None = None
    deleted: bool | None = None
    main_photo_id: int | None = None
    photo_ids: list[Any] | None = None
    video_ids: list[Any] | None = None
    url: str | None = None
    variant_ids: list[Any] | None = None
    is_main_variant: bool | None = None
    dimension_width: int | None = None
    dimension_height: int | None = None
    dimension_length: int | None = None
    weight: int | None = None
    sku: str | None = None
    stock_amount: int | None = None

class MarketEditAlbum(VKMethod[Any]):
    __api_method__ = 'market.editAlbum'
    owner_id: int = ...
    album_id: int = ...
    title: str = ...
    photo_id: int | None = None
    main_album: bool | None = None
    is_hidden: bool | None = None

class MarketEditComment(VKMethod[Any]):
    __api_method__ = 'market.editComment'
    owner_id: int = ...
    comment_id: int = ...
    message: str | None = None
    attachments: list[Any] | None = None

class MarketEditOrder(VKMethod[Any]):
    __api_method__ = 'market.editOrder'
    user_id: int = ...
    order_id: int = ...
    merchant_comment: str | None = None
    status: int | None = None
    track_number: str | None = None
    payment_status: str | None = None
    delivery_price: int | None = None
    width: int | None = None
    length: int | None = None
    height: int | None = None
    weight: int | None = None
    comment_for_user: str | None = None
    receipt_link: str | None = None

class MarketEditProperty(VKMethod[Any]):
    __api_method__ = 'market.editProperty'
    group_id: int = ...
    property_id: int = ...
    title: str = ...

class MarketEditPropertyVariant(VKMethod[Any]):
    __api_method__ = 'market.editPropertyVariant'
    group_id: int = ...
    variant_id: int = ...
    title: str = ...

class MarketFilterCategories(VKMethod[Any]):
    __api_method__ = 'market.filterCategories'
    category_id: int | None = None
    query: str | None = None
    count: int | None = None

class MarketGet(VKMethod[Any]):
    __api_method__ = 'market.get'
    owner_id: int = ...
    album_id: int | None = None
    count: int | None = None
    offset: int | None = None
    extended: bool | None = None
    date_from: str | None = None
    date_to: str | None = None
    need_variants: bool | None = None
    with_disabled: bool | None = None
    fields: list[Any] | None = None

class MarketGetAlbumById(VKMethod[Any]):
    __api_method__ = 'market.getAlbumById'
    owner_id: int = ...
    album_ids: list[Any] = ...

class MarketGetAlbums(VKMethod[Any]):
    __api_method__ = 'market.getAlbums'
    owner_id: int = ...
    offset: int | None = None
    count: int | None = None

class MarketGetById(VKMethod[Any]):
    __api_method__ = 'market.getById'
    item_ids: list[Any] = ...
    extended: bool | None = None

class MarketGetCategories(VKMethod[Any]):
    __api_method__ = 'market.getCategories'
    group_id: int | None = None
    album_id: int | None = None

class MarketGetComments(VKMethod[Any]):
    __api_method__ = 'market.getComments'
    owner_id: int = ...
    item_id: int = ...
    need_likes: bool | None = None
    start_comment_id: int | None = None
    offset: int | None = None
    count: int | None = None
    sort: str | None = None
    extended: bool | None = None
    fields: list[Any] | None = None

class MarketGetFavesForAttach(VKMethod[Any]):
    __api_method__ = 'market.getFavesForAttach'
    current_group_id: int | None = None
    public_only: bool | None = None
    offset: int | None = None
    count: int | None = None

class MarketGetGroupOrders(VKMethod[Any]):
    __api_method__ = 'market.getGroupOrders'
    group_id: int | str | None = None
    offset: int | None = None
    count: int | None = None

class MarketGetOrderById(VKMethod[Any]):
    __api_method__ = 'market.getOrderById'
    user_id: int | None = None
    order_id: int = ...
    extended: bool | None = None

class MarketGetOrderItems(VKMethod[Any]):
    __api_method__ = 'market.getOrderItems'
    user_id: int | None = None
    order_id: int = ...
    offset: int | None = None
    count: int | None = None

class MarketGetOrders(VKMethod[Any]):
    __api_method__ = 'market.getOrders'
    offset: int | None = None
    count: int | None = None
    extended: bool | None = None
    date_from: str | None = None
    date_to: str | None = None

class MarketGetProductPhotoUploadServer(VKMethod[Any]):
    __api_method__ = 'market.getProductPhotoUploadServer'
    group_id: int = ...
    bulk: bool | None = None

class MarketGetProperties(VKMethod[Any]):
    __api_method__ = 'market.getProperties'
    group_id: int = ...

class MarketGroupItems(VKMethod[Any]):
    __api_method__ = 'market.groupItems'
    group_id: int = ...
    item_ids: list[Any] = ...
    item_group_id: int | None = None

class MarketRemoveFromAlbum(VKMethod[Any]):
    __api_method__ = 'market.removeFromAlbum'
    owner_id: int = ...
    item_id: int = ...
    album_ids: list[Any] = ...

class MarketReorderAlbums(VKMethod[Any]):
    __api_method__ = 'market.reorderAlbums'
    owner_id: int = ...
    album_id: int = ...
    before: int | None = None
    after: int | None = None

class MarketReorderItems(VKMethod[Any]):
    __api_method__ = 'market.reorderItems'
    owner_id: int = ...
    album_id: int | None = None
    item_id: int = ...
    before: int | None = None
    after: int | None = None

class MarketReport(VKMethod[Any]):
    __api_method__ = 'market.report'
    owner_id: int = ...
    item_id: int = ...
    reason: int | None = None

class MarketReportComment(VKMethod[Any]):
    __api_method__ = 'market.reportComment'
    owner_id: int = ...
    comment_id: int = ...
    reason: int = ...

class MarketRestore(VKMethod[Any]):
    __api_method__ = 'market.restore'
    owner_id: int = ...
    item_id: int = ...

class MarketRestoreComment(VKMethod[Any]):
    __api_method__ = 'market.restoreComment'
    owner_id: int = ...
    comment_id: int = ...

class MarketSaveProductPhoto(VKMethod[Any]):
    __api_method__ = 'market.saveProductPhoto'
    upload_response: str = ...

class MarketSaveProductPhotoBulk(VKMethod[Any]):
    __api_method__ = 'market.saveProductPhotoBulk'
    upload_response: str = ...

class MarketSearch(VKMethod[Any]):
    __api_method__ = 'market.search'
    owner_id: int = ...
    album_id: int | None = None
    q: str | None = None
    price_from: int | None = None
    price_to: int | None = None
    sort: int | None = None
    rev: int | None = None
    offset: int | None = None
    count: int | None = None
    extended: bool | None = None
    status: list[Any] | None = None
    need_variants: bool | None = None

class MarketSearchItems(VKMethod[Any]):
    __api_method__ = 'market.searchItems'
    q: str = ...
    offset: int | None = None
    count: int | None = None
    category_id: int | None = None
    price_from: int | None = None
    price_to: int | None = None
    sort_by: int | None = None
    sort_direction: int | None = None
    country: int | None = None
    city: int | None = None

class MarketSearchItemsBasic(VKMethod[Any]):
    __api_method__ = 'market.searchItemsBasic'
    q: str = ...
    offset: int | None = None
    count: int | None = None
    category_id: int | None = None
    price_from: int | None = None
    price_to: int | None = None
    sort_by: int | None = None
    sort_direction: int | None = None
    country: int | None = None
    city: int | None = None
    only_my_groups: bool | None = None

class MarketUngroupItems(VKMethod[Any]):
    __api_method__ = 'market.ungroupItems'
    group_id: int = ...
    item_group_id: int = ...

class MessagesAddChatUser(VKMethod[Any]):
    __api_method__ = 'messages.addChatUser'
    chat_id: int = ...
    user_id: int | None = None
    visible_messages_count: int | None = None

class MessagesAddChatUsers(VKMethod[Any]):
    __api_method__ = 'messages.addChatUsers'
    chat_id: int | None = None
    visible_messages_count: int | None = None

class MessagesAllowMessagesFromGroup(VKMethod[Any]):
    __api_method__ = 'messages.allowMessagesFromGroup'
    group_id: int = ...
    key: str | None = None

class MessagesCreateChat(VKMethod[Any]):
    __api_method__ = 'messages.createChat'
    user_ids: list[Any] | None = None
    title: str | None = None
    group_id: int | None = None

class MessagesDelete(VKMethod[Any]):
    __api_method__ = 'messages.delete'
    message_ids: list[Any] | None = None
    spam: bool | None = None
    reason: int | None = None
    group_id: int | None = None
    delete_for_all: bool | None = None
    peer_id: int | None = None
    cmids: list[Any] | None = None

class MessagesDeleteChatPhoto(VKMethod[Any]):
    __api_method__ = 'messages.deleteChatPhoto'
    chat_id: int = ...
    group_id: int | None = None

class MessagesDeleteConversation(VKMethod[Any]):
    __api_method__ = 'messages.deleteConversation'
    user_id: int | None = None
    peer_id: int | None = None
    group_id: int | None = None

class MessagesDeleteReaction(VKMethod[Any]):
    __api_method__ = 'messages.deleteReaction'
    peer_id: int = ...
    cmid: int = ...

class MessagesDenyMessagesFromGroup(VKMethod[Any]):
    __api_method__ = 'messages.denyMessagesFromGroup'
    group_id: int = ...

class MessagesEdit(VKMethod[Any]):
    __api_method__ = 'messages.edit'
    peer_id: int = ...
    message: str | None = None
    lat: float | None = None
    long: float | None = None
    attachment: str | None = None
    keep_forward_messages: bool | None = None
    keep_snippets: bool | None = None
    group_id: int | None = None
    dont_parse_links: bool | None = None
    disable_mentions: bool | None = None
    message_id: int | None = None
    cmid: int | None = None
    template: str | None = None
    keyboard: str | None = None

class MessagesEditChat(VKMethod[Any]):
    __api_method__ = 'messages.editChat'
    chat_id: int = ...
    title: str | None = None

class MessagesGetByConversationMessageId(VKMethod[Any]):
    __api_method__ = 'messages.getByConversationMessageId'
    peer_id: int = ...
    conversation_message_ids: list[Any] = ...
    extended: bool | None = None
    fields: list[Any] | None = None
    group_id: int | None = None

class MessagesGetById(VKMethod[Any]):
    __api_method__ = 'messages.getById'
    message_ids: list[Any] | None = None
    preview_length: int | None = None
    extended: bool | None = None
    fields: list[Any] | None = None
    group_id: int | None = None
    cmids: list[Any] | None = None
    peer_id: int | None = None

class MessagesGetChat(VKMethod[Any]):
    __api_method__ = 'messages.getChat'
    chat_id: int | None = None
    chat_ids: list[Any] | None = None
    fields: list[Any] | None = None
    name_case: str | None = None

class MessagesGetChatPreview(VKMethod[Any]):
    __api_method__ = 'messages.getChatPreview'
    peer_id: int | None = None
    link: str | None = None
    fields: list[Any] | None = None

class MessagesGetConversationMembers(VKMethod[Any]):
    __api_method__ = 'messages.getConversationMembers'
    peer_id: int = ...
    offset: int | None = None
    count: int | None = None
    extended: bool | None = None
    fields: list[Any] | None = None
    group_id: int | None = None
    member_ids: list[Any] | None = None

class MessagesGetConversations(VKMethod[Any]):
    __api_method__ = 'messages.getConversations'
    offset: int | None = None
    count: int | None = None
    filter: str | None = None
    extended: bool | None = None
    start_message_id: int | None = None
    fields: list[Any] | None = None
    group_id: int | None = None

class MessagesGetConversationsById(VKMethod[Any]):
    __api_method__ = 'messages.getConversationsById'
    peer_ids: list[Any] = ...
    extended: bool | None = None
    fields: list[Any] | None = None
    group_id: int | None = None

class MessagesGetHistory(VKMethod[Any]):
    __api_method__ = 'messages.getHistory'
    offset: int | None = None
    count: int | None = None
    user_id: int | None = None
    peer_id: int | None = None
    start_message_id: int | None = None
    rev: int | None = None
    extended: bool | None = None
    fields: list[Any] | None = None
    group_id: int | None = None

class MessagesGetHistoryAttachments(VKMethod[Any]):
    __api_method__ = 'messages.getHistoryAttachments'
    attachment_types: list[Any] | None = None
    group_id: int | None = None
    peer_id: int | None = None
    cmid: int | None = None
    attachment_position: int | None = None
    offset: int | None = None
    count: int | None = None
    extended: bool | None = None
    fields: list[Any] | None = None
    max_forwards_level: int | None = None
    message_video: bool | None = None
    media_type: str | None = None
    start_from: str | None = None
    preserve_order: bool | None = None
    photo_sizes: bool | None = None

class MessagesGetImportantMessages(VKMethod[Any]):
    __api_method__ = 'messages.getImportantMessages'
    count: int | None = None
    offset: int | None = None
    start_message_id: int | None = None
    preview_length: int | None = None
    fields: list[Any] | None = None
    extended: bool | None = None
    group_id: int | None = None

class MessagesGetIntentUsers(VKMethod[Any]):
    __api_method__ = 'messages.getIntentUsers'
    intent: str = ...
    subscribe_id: int | None = None
    offset: int | None = None
    count: int | None = None
    extended: bool | None = None
    name_case: str | None = None
    fields: list[Any] | None = None

class MessagesGetInviteLink(VKMethod[Any]):
    __api_method__ = 'messages.getInviteLink'
    peer_id: int = ...
    reset: bool | None = None
    group_id: int | None = None

class MessagesGetLastActivity(VKMethod[Any]):
    __api_method__ = 'messages.getLastActivity'
    user_id: int = ...

class MessagesGetLongPollHistory(VKMethod[Any]):
    __api_method__ = 'messages.getLongPollHistory'
    ts: int | None = None
    pts: int | None = None
    preview_length: int | None = None
    onlines: bool | None = None
    fields: list[Any] | None = None
    events_limit: int | None = None
    msgs_limit: int | None = None
    max_msg_id: int | None = None
    group_id: int | None = None
    lp_version: int | None = None
    last_n: int | None = None
    credentials: bool | None = None
    extended: bool | None = None

class MessagesGetLongPollServer(VKMethod[Any]):
    __api_method__ = 'messages.getLongPollServer'
    need_pts: bool | None = None
    group_id: int | None = None
    lp_version: int | None = None

class MessagesGetMessagesReactions(VKMethod[Any]):
    __api_method__ = 'messages.getMessagesReactions'
    peer_id: int = ...
    cmids: list[Any] = ...

class MessagesGetReactedPeers(VKMethod[Any]):
    __api_method__ = 'messages.getReactedPeers'
    peer_id: int = ...
    cmid: int = ...
    reaction_id: int | None = None

class MessagesGetReactionsAssets(VKMethod[Any]):
    __api_method__ = 'messages.getReactionsAssets'
    client_version: int | None = None

class MessagesIsMessagesFromGroupAllowed(VKMethod[Any]):
    __api_method__ = 'messages.isMessagesFromGroupAllowed'
    group_id: int = ...
    user_id: int = ...

class MessagesJoinChatByInviteLink(VKMethod[Any]):
    __api_method__ = 'messages.joinChatByInviteLink'
    link: str = ...

class MessagesMarkAsAnsweredConversation(VKMethod[Any]):
    __api_method__ = 'messages.markAsAnsweredConversation'
    peer_id: int = ...
    answered: bool | None = None
    group_id: int | None = None

class MessagesMarkAsImportant(VKMethod[Any]):
    __api_method__ = 'messages.markAsImportant'
    message_ids: list[Any] | None = None
    important: int | None = None

class MessagesMarkAsImportantConversation(VKMethod[Any]):
    __api_method__ = 'messages.markAsImportantConversation'
    peer_id: int = ...
    important: bool | None = None
    group_id: int | None = None

class MessagesMarkAsRead(VKMethod[Any]):
    __api_method__ = 'messages.markAsRead'
    message_ids: list[Any] | None = None
    peer_id: int | None = None
    start_message_id: int | None = None
    group_id: int | None = None
    mark_conversation_as_read: bool | None = None
    up_to_cmid: int | None = None

class MessagesMarkReactionsAsRead(VKMethod[Any]):
    __api_method__ = 'messages.markReactionsAsRead'
    peer_id: int = ...
    cmids: list[Any] | None = None

class MessagesMuteChatMentions(VKMethod[Any]):
    __api_method__ = 'messages.muteChatMentions'
    peer_id: int = ...
    mention_status: str = ...

class MessagesPin(VKMethod[Any]):
    __api_method__ = 'messages.pin'
    peer_id: int = ...
    message_id: int | None = None
    cmid: int | None = None

class MessagesRemoveChatUser(VKMethod[Any]):
    __api_method__ = 'messages.removeChatUser'
    chat_id: int = ...
    user_id: int | None = None
    member_id: int | None = None

class MessagesRestore(VKMethod[Any]):
    __api_method__ = 'messages.restore'
    message_id: int | None = None
    group_id: int | None = None
    cmid: int | None = None
    peer_id: int | None = None

class MessagesSearch(VKMethod[Any]):
    __api_method__ = 'messages.search'
    q: str | None = None
    peer_id: int | None = None
    date: int | None = None
    preview_length: int | None = None
    offset: int | None = None
    count: int | None = None
    extended: bool | None = None
    fields: list[Any] | None = None
    group_id: int | None = None

class MessagesSearchConversations(VKMethod[Any]):
    __api_method__ = 'messages.searchConversations'
    q: str | None = None
    count: int | None = None
    extended: bool | None = None
    fields: list[Any] | None = None
    group_id: int | None = None

class MessagesSend(VKMethod[Any]):
    __api_method__ = 'messages.send'
    user_id: int | None = None
    random_id: int | None = None
    peer_id: int | None = None
    peer_ids: list[Any] | None = None
    domain: str | None = None
    chat_id: int | None = None
    message: str | None = None
    lat: float | None = None
    long: float | None = None
    attachment: str | None = None
    reply_to: int | None = None
    forward_messages: list[Any] | None = None
    forward: str | None = None
    sticker_id: int | None = None
    group_id: int | None = None
    keyboard: str | None = None
    template: str | None = None
    payload: str | None = None
    content_source: str | None = None
    dont_parse_links: bool | None = None
    disable_mentions: bool | None = None
    intent: str | None = None
    subscribe_id: int | None = None

class MessagesSendMessageEventAnswer(VKMethod[Any]):
    __api_method__ = 'messages.sendMessageEventAnswer'
    event_id: str = ...
    user_id: int = ...
    peer_id: int = ...
    event_data: str | None = None

class MessagesSendReaction(VKMethod[Any]):
    __api_method__ = 'messages.sendReaction'
    peer_id: int = ...
    cmid: int = ...
    reaction_id: int = ...

class MessagesSetActivity(VKMethod[Any]):
    __api_method__ = 'messages.setActivity'
    user_id: int | None = None
    type: str | None = None
    peer_id: int | None = None
    group_id: int | None = None

class MessagesSetChatPhoto(VKMethod[Any]):
    __api_method__ = 'messages.setChatPhoto'
    file: str = ...

class MessagesUnpin(VKMethod[Any]):
    __api_method__ = 'messages.unpin'
    peer_id: int = ...
    group_id: int | None = None

class NewsfeedAddBan(VKMethod[Any]):
    __api_method__ = 'newsfeed.addBan'
    user_ids: list[Any] | None = None
    group_ids: list[Any] | None = None

class NewsfeedDeleteBan(VKMethod[Any]):
    __api_method__ = 'newsfeed.deleteBan'
    user_ids: list[Any] | None = None
    group_ids: list[Any] | None = None

class NewsfeedDeleteList(VKMethod[Any]):
    __api_method__ = 'newsfeed.deleteList'
    list_id: int = ...

class NewsfeedGet(VKMethod[Any]):
    __api_method__ = 'newsfeed.get'
    filters: list[Any] | None = None
    return_banned: bool | None = None
    start_time: int | None = None
    end_time: int | None = None
    max_photos: int | None = None
    source_ids: str | None = None
    start_from: str | None = None
    count: int | None = None
    fields: list[Any] | None = None
    section: str | None = None

class NewsfeedGetBanned(VKMethod[Any]):
    __api_method__ = 'newsfeed.getBanned'
    extended: bool | None = None
    fields: list[Any] | None = None
    name_case: str | None = None

class NewsfeedGetComments(VKMethod[Any]):
    __api_method__ = 'newsfeed.getComments'
    count: int | None = None
    filters: list[Any] | None = None
    reposts: str | None = None
    start_time: int | None = None
    end_time: int | None = None
    last_comments_count: int | None = None
    start_from: str | None = None
    fields: list[Any] | None = None

class NewsfeedGetLists(VKMethod[Any]):
    __api_method__ = 'newsfeed.getLists'
    list_ids: list[Any] | None = None
    extended: bool | None = None

class NewsfeedGetMentions(VKMethod[Any]):
    __api_method__ = 'newsfeed.getMentions'
    owner_id: int | None = None
    start_time: int | None = None
    end_time: int | None = None
    offset: int | None = None
    count: int | None = None

class NewsfeedGetRecommended(VKMethod[Any]):
    __api_method__ = 'newsfeed.getRecommended'
    start_time: int | None = None
    end_time: int | None = None
    max_photos: int | None = None
    start_from: str | None = None
    count: int | None = None
    fields: list[Any] | None = None

class NewsfeedGetSuggestedSources(VKMethod[Any]):
    __api_method__ = 'newsfeed.getSuggestedSources'
    offset: int | None = None
    count: int | None = None
    shuffle: bool | None = None
    fields: list[Any] | None = None

class NewsfeedIgnoreItem(VKMethod[Any]):
    __api_method__ = 'newsfeed.ignoreItem'
    type: str = ...
    owner_id: int | None = None
    item_id: int | None = None

class NewsfeedSaveList(VKMethod[Any]):
    __api_method__ = 'newsfeed.saveList'
    list_id: int | None = None
    title: str = ...
    source_ids: list[Any] = ...
    no_reposts: bool | None = None

class NewsfeedSearch(VKMethod[Any]):
    __api_method__ = 'newsfeed.search'
    q: str | None = None
    extended: bool | None = None
    count: int | None = None
    latitude: float | None = None
    longitude: float | None = None
    start_time: int | None = None
    end_time: int | None = None
    start_from: str | None = None
    fields: list[Any] | None = None

class NewsfeedUnignoreItem(VKMethod[Any]):
    __api_method__ = 'newsfeed.unignoreItem'
    type: str = ...
    owner_id: int | None = None
    item_id: int | None = None
    track_code: str | None = None

class NewsfeedUnsubscribe(VKMethod[Any]):
    __api_method__ = 'newsfeed.unsubscribe'
    type: str = ...
    owner_id: int | None = None
    item_id: int = ...

class NotesAdd(VKMethod[Any]):
    __api_method__ = 'notes.add'
    title: str = ...
    text: str = ...
    privacy_view: list[Any] | None = None
    privacy_comment: list[Any] | None = None

class NotesCreateComment(VKMethod[Any]):
    __api_method__ = 'notes.createComment'
    note_id: int = ...
    owner_id: int | None = None
    reply_to: int | None = None
    message: str = ...
    guid: str | None = None

class NotesDelete(VKMethod[Any]):
    __api_method__ = 'notes.delete'
    note_id: int = ...

class NotesDeleteComment(VKMethod[Any]):
    __api_method__ = 'notes.deleteComment'
    comment_id: int = ...
    owner_id: int | None = None

class NotesEdit(VKMethod[Any]):
    __api_method__ = 'notes.edit'
    note_id: int = ...
    title: str = ...
    text: str = ...
    privacy_view: list[Any] | None = None
    privacy_comment: list[Any] | None = None

class NotesEditComment(VKMethod[Any]):
    __api_method__ = 'notes.editComment'
    comment_id: int = ...
    owner_id: int | None = None
    message: str = ...

class NotesGet(VKMethod[Any]):
    __api_method__ = 'notes.get'
    note_ids: list[Any] | None = None
    user_id: int | None = None
    offset: int | None = None
    count: int | None = None
    sort: int | None = None

class NotesGetById(VKMethod[Any]):
    __api_method__ = 'notes.getById'
    note_id: int = ...
    owner_id: int | None = None
    need_wiki: bool | None = None

class NotesGetComments(VKMethod[Any]):
    __api_method__ = 'notes.getComments'
    note_id: int = ...
    owner_id: int | None = None
    sort: int | None = None
    offset: int | None = None
    count: int | None = None

class NotesRestoreComment(VKMethod[Any]):
    __api_method__ = 'notes.restoreComment'
    comment_id: int = ...
    owner_id: int | None = None

class NotificationsGet(VKMethod[Any]):
    __api_method__ = 'notifications.get'
    count: int | None = None
    start_from: str | None = None
    filters: list[Any] | None = None
    start_time: int | None = None
    end_time: int | None = None

class NotificationsMarkAsViewed(VKMethod[Any]):
    __api_method__ = 'notifications.markAsViewed'
    pass

class NotificationsSendMessage(VKMethod[Any]):
    __api_method__ = 'notifications.sendMessage'
    user_ids: list[Any] = ...
    message: str = ...
    fragment: str | None = None
    group_id: int | None = None
    random_id: int | None = None
    sending_mode: str | None = None

class OrdersCancelSubscription(VKMethod[Any]):
    __api_method__ = 'orders.cancelSubscription'
    user_id: int = ...
    subscription_id: int = ...
    pending_cancel: bool | None = None

class OrdersChangeState(VKMethod[Any]):
    __api_method__ = 'orders.changeState'
    order_id: int = ...
    action: str = ...
    app_order_id: int | None = None
    test_mode: bool | None = None

class OrdersGet(VKMethod[Any]):
    __api_method__ = 'orders.get'
    offset: int | None = None
    count: int | None = None
    test_mode: bool | None = None

class OrdersGetAmount(VKMethod[Any]):
    __api_method__ = 'orders.getAmount'
    user_id: int = ...
    votes: list[Any] = ...

class OrdersGetById(VKMethod[Any]):
    __api_method__ = 'orders.getById'
    order_id: int | None = None
    order_ids: list[Any] | None = None
    test_mode: bool | None = None

class OrdersGetUserSubscriptionById(VKMethod[Any]):
    __api_method__ = 'orders.getUserSubscriptionById'
    user_id: int = ...
    subscription_id: int = ...

class OrdersGetUserSubscriptions(VKMethod[Any]):
    __api_method__ = 'orders.getUserSubscriptions'
    user_id: int = ...

class PagesClearCache(VKMethod[Any]):
    __api_method__ = 'pages.clearCache'
    url: str = ...

class PagesGet(VKMethod[Any]):
    __api_method__ = 'pages.get'
    owner_id: int | None = None
    page_id: int | None = None
    global_: bool | None = Field(default=None, alias='global')
    site_preview: bool | None = None
    title: str | None = None
    need_source: bool | None = None
    need_html: bool | None = None

class PagesGetHistory(VKMethod[Any]):
    __api_method__ = 'pages.getHistory'
    page_id: int = ...
    group_id: int | None = None
    user_id: int | None = None

class PagesGetTitles(VKMethod[Any]):
    __api_method__ = 'pages.getTitles'
    group_id: int | None = None

class PagesGetVersion(VKMethod[Any]):
    __api_method__ = 'pages.getVersion'
    version_id: int = ...
    group_id: int | None = None
    user_id: int | None = None
    need_html: bool | None = None

class PagesParseWiki(VKMethod[Any]):
    __api_method__ = 'pages.parseWiki'
    text: str = ...
    group_id: int | None = None

class PagesSave(VKMethod[Any]):
    __api_method__ = 'pages.save'
    text: str | None = None
    page_id: int | None = None
    group_id: int | None = None
    user_id: int | None = None
    title: str | None = None

class PagesSaveAccess(VKMethod[Any]):
    __api_method__ = 'pages.saveAccess'
    page_id: int = ...
    group_id: int | None = None
    user_id: int | None = None
    view: int | None = None
    edit: int | None = None

class PhotosConfirmTag(VKMethod[Any]):
    __api_method__ = 'photos.confirmTag'
    owner_id: int | None = None
    photo_id: str = ...
    tag_id: int = ...

class PhotosCopy(VKMethod[Any]):
    __api_method__ = 'photos.copy'
    owner_id: int = ...
    photo_id: int = ...
    access_key: str | None = None

class PhotosCreateAlbum(VKMethod[Any]):
    __api_method__ = 'photos.createAlbum'
    title: str = ...
    group_id: int | None = None
    description: str | None = None
    privacy_view: list[Any] | None = None
    privacy_comment: list[Any] | None = None
    upload_by_admins_only: bool | None = None
    comments_disabled: bool | None = None

class PhotosCreateComment(VKMethod[Any]):
    __api_method__ = 'photos.createComment'
    owner_id: int | None = None
    photo_id: int = ...
    message: str | None = None
    attachments: list[Any] | None = None
    from_group: bool | None = None
    reply_to_comment: int | None = None
    sticker_id: int | None = None
    access_key: str | None = None
    guid: str | None = None

class PhotosDelete(VKMethod[Any]):
    __api_method__ = 'photos.delete'
    owner_id: int | None = None
    photo_id: int | None = None
    photos: list[Any] | None = None

class PhotosDeleteAlbum(VKMethod[Any]):
    __api_method__ = 'photos.deleteAlbum'
    album_id: int = ...
    group_id: int | None = None

class PhotosDeleteComment(VKMethod[Any]):
    __api_method__ = 'photos.deleteComment'
    owner_id: int | None = None
    comment_id: int = ...

class PhotosEdit(VKMethod[Any]):
    __api_method__ = 'photos.edit'
    owner_id: int | None = None
    photo_id: int = ...
    caption: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    place_str: str | None = None
    foursquare_id: str | None = None
    delete_place: bool | None = None

class PhotosEditAlbum(VKMethod[Any]):
    __api_method__ = 'photos.editAlbum'
    album_id: int = ...
    title: str | None = None
    description: str | None = None
    owner_id: int | None = None
    privacy_view: list[Any] | None = None
    privacy_comment: list[Any] | None = None
    upload_by_admins_only: bool | None = None
    comments_disabled: bool | None = None

class PhotosEditComment(VKMethod[Any]):
    __api_method__ = 'photos.editComment'
    owner_id: int | None = None
    comment_id: int = ...
    message: str | None = None
    attachments: list[Any] | None = None

class PhotosGet(VKMethod[Any]):
    __api_method__ = 'photos.get'
    owner_id: int | None = None
    album_id: str | None = None
    photo_ids: list[Any] | None = None
    rev: bool | None = None
    extended: bool | None = None
    feed_type: str | None = None
    feed: int | None = None
    photo_sizes: bool | None = None
    offset: int | None = None
    count: int | None = None

class PhotosGetAlbums(VKMethod[Any]):
    __api_method__ = 'photos.getAlbums'
    owner_id: int | None = None
    album_ids: list[Any] | None = None
    offset: int | None = None
    count: int | None = None
    need_system: bool | None = None
    need_covers: bool | None = None
    photo_sizes: bool | None = None

class PhotosGetAlbumsCount(VKMethod[Any]):
    __api_method__ = 'photos.getAlbumsCount'
    user_id: int | None = None
    group_id: int | None = None
    need_system: bool | None = None

class PhotosGetAll(VKMethod[Any]):
    __api_method__ = 'photos.getAll'
    owner_id: int | None = None
    extended: bool | None = None
    offset: int | None = None
    count: int | None = None
    photo_sizes: bool | None = None
    no_service_albums: bool | None = None
    need_hidden: bool | None = None
    skip_hidden: bool | None = None

class PhotosGetAllComments(VKMethod[Any]):
    __api_method__ = 'photos.getAllComments'
    owner_id: int | None = None
    album_id: int | None = None
    need_likes: bool | None = None
    offset: int | None = None
    count: int | None = None

class PhotosGetById(VKMethod[Any]):
    __api_method__ = 'photos.getById'
    photos: list[Any] = ...
    extended: bool | None = None
    photo_sizes: bool | None = None

class PhotosGetChatUploadServer(VKMethod[Any]):
    __api_method__ = 'photos.getChatUploadServer'
    chat_id: int = ...
    crop_x: int | None = None
    crop_y: int | None = None
    crop_width: int | None = None

class PhotosGetComments(VKMethod[Any]):
    __api_method__ = 'photos.getComments'
    owner_id: int | None = None
    photo_id: int = ...
    need_likes: bool | None = None
    start_comment_id: int | None = None
    offset: int | None = None
    count: int | None = None
    sort: str | None = None
    access_key: str | None = None
    extended: bool | None = None
    fields: list[Any] | None = None

class PhotosGetMarketAlbumUploadServer(VKMethod[Any]):
    __api_method__ = 'photos.getMarketAlbumUploadServer'
    group_id: int = ...

class PhotosGetMessagesUploadServer(VKMethod[Any]):
    __api_method__ = 'photos.getMessagesUploadServer'
    peer_id: int | None = None

class PhotosGetNewTags(VKMethod[Any]):
    __api_method__ = 'photos.getNewTags'
    offset: int | None = None
    count: int | None = None

class PhotosGetOwnerCoverPhotoUploadServer(VKMethod[Any]):
    __api_method__ = 'photos.getOwnerCoverPhotoUploadServer'
    group_id: int | None = None
    crop_x: int | None = None
    crop_y: int | None = None
    crop_x2: int | None = None
    crop_y2: int | None = None
    is_video_cover: bool | None = None

class PhotosGetOwnerPhotoUploadServer(VKMethod[Any]):
    __api_method__ = 'photos.getOwnerPhotoUploadServer'
    owner_id: int | None = None

class PhotosGetTags(VKMethod[Any]):
    __api_method__ = 'photos.getTags'
    owner_id: int | None = None
    photo_id: int = ...
    access_key: str | None = None

class PhotosGetUploadServer(VKMethod[Any]):
    __api_method__ = 'photos.getUploadServer'
    album_id: int | None = None
    group_id: int | None = None

class PhotosGetUserPhotos(VKMethod[Any]):
    __api_method__ = 'photos.getUserPhotos'
    user_id: int | None = None
    offset: int | None = None
    count: int | None = None
    extended: bool | None = None
    sort: str | None = None

class PhotosGetWallUploadServer(VKMethod[Any]):
    __api_method__ = 'photos.getWallUploadServer'
    group_id: int | None = None

class PhotosMakeCover(VKMethod[Any]):
    __api_method__ = 'photos.makeCover'
    owner_id: int | None = None
    photo_id: int = ...
    album_id: int | None = None

class PhotosMove(VKMethod[Any]):
    __api_method__ = 'photos.move'
    owner_id: int | None = None
    target_album_id: int = ...
    photo_ids: list[Any] = ...

class PhotosPutTag(VKMethod[Any]):
    __api_method__ = 'photos.putTag'
    owner_id: int | None = None
    photo_id: int = ...
    user_id: int = ...
    x: float | None = None
    y: float | None = None
    x2: float | None = None
    y2: float | None = None

class PhotosRemoveTag(VKMethod[Any]):
    __api_method__ = 'photos.removeTag'
    owner_id: int | None = None
    photo_id: int = ...
    tag_id: int = ...

class PhotosReorderAlbums(VKMethod[Any]):
    __api_method__ = 'photos.reorderAlbums'
    owner_id: int | None = None
    album_id: int = ...
    before: int | None = None
    after: int | None = None

class PhotosReorderPhotos(VKMethod[Any]):
    __api_method__ = 'photos.reorderPhotos'
    owner_id: int | None = None
    photo_id: int = ...
    before: int | None = None
    after: int | None = None

class PhotosReport(VKMethod[Any]):
    __api_method__ = 'photos.report'
    owner_id: int = ...
    photo_id: int = ...
    reason: int | None = None

class PhotosReportComment(VKMethod[Any]):
    __api_method__ = 'photos.reportComment'
    owner_id: int = ...
    comment_id: int = ...
    reason: int | None = None

class PhotosRestore(VKMethod[Any]):
    __api_method__ = 'photos.restore'
    owner_id: int | None = None
    photo_id: int = ...

class PhotosRestoreComment(VKMethod[Any]):
    __api_method__ = 'photos.restoreComment'
    owner_id: int | None = None
    comment_id: int = ...

class PhotosSave(VKMethod[Any]):
    __api_method__ = 'photos.save'
    album_id: int | None = None
    group_id: int | None = None
    server: int | None = None
    photos_list: str | None = None
    hash: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    caption: str | None = None

class PhotosSaveMarketAlbumPhoto(VKMethod[Any]):
    __api_method__ = 'photos.saveMarketAlbumPhoto'
    group_id: int = ...
    photo: str = ...
    server: int = ...
    hash: str = ...

class PhotosSaveMessagesPhoto(VKMethod[Any]):
    __api_method__ = 'photos.saveMessagesPhoto'
    photo: str = ...
    server: int | None = None
    hash: str | None = None

class PhotosSaveOwnerCoverPhoto(VKMethod[Any]):
    __api_method__ = 'photos.saveOwnerCoverPhoto'
    crop_x: int | None = None
    crop_height: int | None = None
    crop_y: int | None = None
    crop_width: int | None = None
    response_json: str | None = None
    hash: str | None = None
    photo: str | None = None
    is_video_cover: bool | None = None

class PhotosSaveOwnerPhoto(VKMethod[Any]):
    __api_method__ = 'photos.saveOwnerPhoto'
    server: str | None = None
    hash: str | None = None
    photo: str | None = None

class PhotosSaveWallPhoto(VKMethod[Any]):
    __api_method__ = 'photos.saveWallPhoto'
    user_id: int | None = None
    group_id: int | None = None
    photo: str = ...
    server: int | None = None
    hash: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    caption: str | None = None

class PhotosSearch(VKMethod[Any]):
    __api_method__ = 'photos.search'
    q: str | None = None
    lat: float | None = None
    long: float | None = None
    start_time: float | None = None
    end_time: float | None = None
    sort: int | None = None
    offset: int | None = None
    count: int | None = None
    radius: int | None = None

class PodcastsSearchPodcast(VKMethod[Any]):
    __api_method__ = 'podcasts.searchPodcast'
    search_string: str = ...
    offset: int | None = None
    count: int | None = None

class PollsAddVote(VKMethod[Any]):
    __api_method__ = 'polls.addVote'
    owner_id: int | None = None
    poll_id: int = ...
    answer_ids: list[Any] = ...
    is_board: bool | None = None

class PollsCreate(VKMethod[Any]):
    __api_method__ = 'polls.create'
    question: str | None = None
    is_anonymous: bool | None = None
    is_multiple: bool | None = None
    end_date: int | None = None
    owner_id: int | None = None
    app_id: int | None = None
    add_answers: str | None = None
    photo_id: int | None = None
    background_id: str | None = None
    disable_unvote: bool | None = None

class PollsDeleteVote(VKMethod[Any]):
    __api_method__ = 'polls.deleteVote'
    owner_id: int | None = None
    poll_id: int = ...
    is_board: bool | None = None

class PollsEdit(VKMethod[Any]):
    __api_method__ = 'polls.edit'
    owner_id: int | None = None
    poll_id: int = ...
    question: str | None = None
    add_answers: str | None = None
    edit_answers: str | None = None
    delete_answers: str | None = None
    end_date: int | None = None
    photo_id: int | None = None
    background_id: str | None = None

class PollsGetBackgrounds(VKMethod[Any]):
    __api_method__ = 'polls.getBackgrounds'
    pass

class PollsGetById(VKMethod[Any]):
    __api_method__ = 'polls.getById'
    owner_id: int | None = None
    is_board: bool | None = None
    poll_id: int = ...
    extended: bool | None = None
    friends_count: int | None = None
    fields: list[Any] | None = None
    name_case: str | None = None

class PollsGetPhotoUploadServer(VKMethod[Any]):
    __api_method__ = 'polls.getPhotoUploadServer'
    owner_id: int | None = None

class PollsGetVoters(VKMethod[Any]):
    __api_method__ = 'polls.getVoters'
    owner_id: int | None = None
    poll_id: int = ...
    answer_ids: list[Any] = ...
    is_board: bool | None = None
    friends_only: bool | None = None
    offset: int | None = None
    count: int | None = None
    fields: list[Any] | None = None
    name_case: str | None = None

class PollsSavePhoto(VKMethod[Any]):
    __api_method__ = 'polls.savePhoto'
    photo: str | None = None
    hash: str | None = None

class PrettyCardsCreate(VKMethod[Any]):
    __api_method__ = 'prettyCards.create'
    owner_id: int = ...
    photo: str = ...
    title: str = ...
    link: str = ...
    price: str | None = None
    price_old: str | None = None
    button: str | None = None

class PrettyCardsDelete(VKMethod[Any]):
    __api_method__ = 'prettyCards.delete'
    owner_id: int = ...
    card_id: int = ...

class PrettyCardsEdit(VKMethod[Any]):
    __api_method__ = 'prettyCards.edit'
    owner_id: int = ...
    card_id: int = ...
    photo: str | None = None
    title: str | None = None
    link: str | None = None
    price: str | None = None
    price_old: str | None = None
    button: str | None = None

class PrettyCardsGet(VKMethod[Any]):
    __api_method__ = 'prettyCards.get'
    owner_id: int = ...
    offset: int | None = None
    count: int | None = None

class PrettyCardsGetById(VKMethod[Any]):
    __api_method__ = 'prettyCards.getById'
    owner_id: int = ...
    card_ids: list[Any] = ...

class PrettyCardsGetUploadURL(VKMethod[Any]):
    __api_method__ = 'prettyCards.getUploadURL'
    pass

class SearchGetHints(VKMethod[Any]):
    __api_method__ = 'search.getHints'
    q: str | None = None
    offset: int | None = None
    limit: int | None = None
    filters: list[Any] | None = None
    fields: list[Any] | None = None
    search_global: bool | None = None

class SecureAddAppEvent(VKMethod[Any]):
    __api_method__ = 'secure.addAppEvent'
    user_id: int | None = None
    activity_id: int = ...
    value: int | None = None

class SecureCheckToken(VKMethod[Any]):
    __api_method__ = 'secure.checkToken'
    token: str | None = None
    ip: str | None = None

class SecureGetAppBalance(VKMethod[Any]):
    __api_method__ = 'secure.getAppBalance'
    pass

class SecureGetSMSHistory(VKMethod[Any]):
    __api_method__ = 'secure.getSMSHistory'
    user_id: int | None = None
    date_from: int | None = None
    date_to: int | None = None
    limit: int | None = None

class SecureGetTransactionsHistory(VKMethod[Any]):
    __api_method__ = 'secure.getTransactionsHistory'
    type: int | None = None
    uid_from: int | None = None
    uid_to: int | None = None
    date_from: int | None = None
    date_to: int | None = None
    limit: int | None = None

class SecureGetUserLevel(VKMethod[Any]):
    __api_method__ = 'secure.getUserLevel'
    user_ids: list[Any] = ...

class SecureGiveEventSticker(VKMethod[Any]):
    __api_method__ = 'secure.giveEventSticker'
    user_ids: list[Any] = ...
    achievement_id: int = ...

class SecureSendNotification(VKMethod[Any]):
    __api_method__ = 'secure.sendNotification'
    user_ids: list[Any] | None = None
    user_id: int | None = None
    message: str = ...
    notification_id: int | None = None
    promo_id: int | None = None

class SecureSendSMSNotification(VKMethod[Any]):
    __api_method__ = 'secure.sendSMSNotification'
    user_id: int = ...
    message: str = ...

class SecureSetCounter(VKMethod[Any]):
    __api_method__ = 'secure.setCounter'
    counters: list[Any] | None = None
    user_id: int | None = None
    counter: int | None = None
    increment: bool | None = None

class StatsGet(VKMethod[Any]):
    __api_method__ = 'stats.get'
    group_id: int | None = None
    app_id: int | None = None
    timestamp_from: float | None = None
    timestamp_to: float | None = None
    interval: str | None = None
    intervals_count: int | None = None
    filters: list[Any] | None = None
    stats_groups: list[Any] | None = None
    extended: bool | None = None

class StatsGetPostReach(VKMethod[Any]):
    __api_method__ = 'stats.getPostReach'
    owner_id: int = ...
    post_ids: list[Any] = ...

class StatsTrackVisitor(VKMethod[Any]):
    __api_method__ = 'stats.trackVisitor'
    type: str | None = None

class StatusGet(VKMethod[Any]):
    __api_method__ = 'status.get'
    user_id: int | None = None
    group_id: int | None = None

class StatusSet(VKMethod[Any]):
    __api_method__ = 'status.set'
    text: str | None = None
    group_id: int | None = None

class StorageGet(VKMethod[Any]):
    __api_method__ = 'storage.get'
    key: str | None = None
    keys: list[Any] | None = None
    user_id: int | None = None

class StorageGetKeys(VKMethod[Any]):
    __api_method__ = 'storage.getKeys'
    user_id: int | None = None
    offset: int | None = None
    count: int | None = None

class StorageSet(VKMethod[Any]):
    __api_method__ = 'storage.set'
    key: str = ...
    value: str | None = None
    user_id: int | None = None

class StoreAddStickersToFavorite(VKMethod[Any]):
    __api_method__ = 'store.addStickersToFavorite'
    sticker_ids: list[Any] = ...

class StoreGetFavoriteStickers(VKMethod[Any]):
    __api_method__ = 'store.getFavoriteStickers'
    pass

class StoreGetProducts(VKMethod[Any]):
    __api_method__ = 'store.getProducts'
    type: str | None = None
    merchant: str | None = None
    section: str | None = None
    product_ids: list[Any] | None = None
    filters: list[Any] | None = None
    extended: bool | None = None

class StoreGetStickersKeywords(VKMethod[Any]):
    __api_method__ = 'store.getStickersKeywords'
    stickers_ids: list[Any] | None = None
    products_ids: list[Any] | None = None
    aliases: bool | None = None
    all_products: bool | None = None
    need_stickers: bool | None = None
    vmoji_promo: bool | None = None

class StoreRemoveStickersFromFavorite(VKMethod[Any]):
    __api_method__ = 'store.removeStickersFromFavorite'
    sticker_ids: list[Any] = ...

class StoriesBanOwner(VKMethod[Any]):
    __api_method__ = 'stories.banOwner'
    owners_ids: list[Any] = ...

class StoriesDelete(VKMethod[Any]):
    __api_method__ = 'stories.delete'
    owner_id: int | None = None
    story_id: int | None = None
    stories: list[Any] | None = None

class StoriesGet(VKMethod[Any]):
    __api_method__ = 'stories.get'
    owner_id: int | None = None
    extended: bool | None = None
    fields: list[Any] | None = None

class StoriesGetBanned(VKMethod[Any]):
    __api_method__ = 'stories.getBanned'
    extended: bool | None = None
    fields: list[Any] | None = None

class StoriesGetById(VKMethod[Any]):
    __api_method__ = 'stories.getById'
    stories: list[Any] = ...
    extended: bool | None = None
    fields: list[Any] | None = None

class StoriesGetPhotoUploadServer(VKMethod[Any]):
    __api_method__ = 'stories.getPhotoUploadServer'
    add_to_news: bool | None = None
    user_ids: list[Any] | None = None
    reply_to_story: str | None = None
    link_text: str | None = None
    link_url: str | None = None
    group_id: int | None = None
    clickable_stickers: str | None = None

class StoriesGetReplies(VKMethod[Any]):
    __api_method__ = 'stories.getReplies'
    owner_id: int = ...
    story_id: int = ...
    access_key: str | None = None
    extended: bool | None = None
    fields: list[Any] | None = None

class StoriesGetStats(VKMethod[Any]):
    __api_method__ = 'stories.getStats'
    owner_id: int = ...
    story_id: int = ...

class StoriesGetVideoUploadServer(VKMethod[Any]):
    __api_method__ = 'stories.getVideoUploadServer'
    add_to_news: bool | None = None
    user_ids: list[Any] | None = None
    reply_to_story: str | None = None
    link_text: str | None = None
    link_url: str | None = None
    group_id: int | None = None
    clickable_stickers: str | None = None

class StoriesGetViewers(VKMethod[Any]):
    __api_method__ = 'stories.getViewers'
    owner_id: int | None = None
    story_id: int = ...
    count: int | None = None
    offset: int | None = None
    extended: bool | None = None
    fields: list[Any] | None = None

class StoriesHideAllReplies(VKMethod[Any]):
    __api_method__ = 'stories.hideAllReplies'
    owner_id: int = ...
    group_id: int | None = None

class StoriesHideReply(VKMethod[Any]):
    __api_method__ = 'stories.hideReply'
    owner_id: int = ...
    story_id: int = ...

class StoriesSave(VKMethod[Any]):
    __api_method__ = 'stories.save'
    upload_results: list[Any] | None = None
    upload_results_json: str | None = None
    extended: bool | None = None
    fields: list[Any] | None = None

class StoriesSearch(VKMethod[Any]):
    __api_method__ = 'stories.search'
    q: str | None = None
    place_id: int | None = None
    latitude: float | None = None
    longitude: float | None = None
    radius: int | None = None
    mentioned_id: int | None = None
    count: int | None = None
    extended: bool | None = None
    fields: list[Any] | None = None

class StoriesSendInteraction(VKMethod[Any]):
    __api_method__ = 'stories.sendInteraction'
    access_key: str = ...
    message: str | None = None
    is_broadcast: bool | None = None
    is_anonymous: bool | None = None
    unseen_marker: bool | None = None

class StoriesUnbanOwner(VKMethod[Any]):
    __api_method__ = 'stories.unbanOwner'
    owners_ids: list[Any] = ...

class StreamingGetServerUrl(VKMethod[Any]):
    __api_method__ = 'streaming.getServerUrl'
    pass

class StreamingGetStats(VKMethod[Any]):
    __api_method__ = 'streaming.getStats'
    type: str | None = None
    interval: str | None = None
    start_time: int | None = None
    end_time: int | None = None

class StreamingGetStem(VKMethod[Any]):
    __api_method__ = 'streaming.getStem'
    word: str = ...

class TranslationsTranslate(VKMethod[Any]):
    __api_method__ = 'translations.translate'
    texts: list[Any] = ...
    translation_language: str = ...

class UsersGet(VKMethod[Any]):
    __api_method__ = 'users.get'
    user_ids: list[Any] | None = None
    fields: list[Any] | None = None
    name_case: str | None = None
    from_group_id: int | None = None

class UsersGetFollowers(VKMethod[Any]):
    __api_method__ = 'users.getFollowers'
    user_id: int | None = None
    offset: int | None = None
    count: int | None = None
    fields: list[Any] | None = None
    name_case: str | None = None

class UsersGetSubscriptions(VKMethod[Any]):
    __api_method__ = 'users.getSubscriptions'
    user_id: int | None = None
    extended: bool | None = None
    offset: int | None = None
    count: int | None = None
    fields: list[Any] | None = None

class UsersReport(VKMethod[Any]):
    __api_method__ = 'users.report'
    user_id: int = ...
    type: str = ...
    comment: str | None = None

class UsersSearch(VKMethod[Any]):
    __api_method__ = 'users.search'
    q: str | None = None
    sort: int | None = None
    offset: int | None = None
    count: int | None = None
    fields: list[Any] | None = None
    city: int | None = None
    city_id: int | None = None
    country: int | None = None
    country_id: int | None = None
    hometown: str | None = None
    university_country: int | None = None
    university: int | None = None
    university_year: int | None = None
    university_faculty: int | None = None
    university_chair: int | None = None
    sex: int | None = None
    status: int | None = None
    age_from: int | None = None
    age_to: int | None = None
    birth_day: int | None = None
    birth_month: int | None = None
    birth_year: int | None = None
    online: bool | None = None
    has_photo: bool | None = None
    school_country: int | None = None
    school_city: int | None = None
    school_class: int | None = None
    school: int | None = None
    school_year: int | None = None
    religion: str | None = None
    company: str | None = None
    position: str | None = None
    group_id: int | None = None
    from_list: list[Any] | None = None
    screen_ref: str | None = None
    from_group_id: int | None = None

class UtilsCheckLink(VKMethod[Any]):
    __api_method__ = 'utils.checkLink'
    url: str = ...

class UtilsDeleteFromLastShortened(VKMethod[Any]):
    __api_method__ = 'utils.deleteFromLastShortened'
    key: str = ...

class UtilsGetLastShortenedLinks(VKMethod[Any]):
    __api_method__ = 'utils.getLastShortenedLinks'
    count: int | None = None
    offset: int | None = None

class UtilsGetLinkStats(VKMethod[Any]):
    __api_method__ = 'utils.getLinkStats'
    key: str = ...
    source: str | None = None
    access_key: str | None = None
    interval: str | None = None
    intervals_count: int | None = None
    extended: bool | None = None

class UtilsGetServerTime(VKMethod[Any]):
    __api_method__ = 'utils.getServerTime'
    pass

class UtilsGetShortLink(VKMethod[Any]):
    __api_method__ = 'utils.getShortLink'
    url: str = ...
    private: bool | None = None

class UtilsResolveScreenName(VKMethod[Any]):
    __api_method__ = 'utils.resolveScreenName'
    screen_name: str = ...

class VideoAdd(VKMethod[Any]):
    __api_method__ = 'video.add'
    target_id: int | None = None
    video_id: int = ...
    owner_id: int = ...

class VideoAddAlbum(VKMethod[Any]):
    __api_method__ = 'video.addAlbum'
    group_id: int | None = None
    title: str | None = None
    privacy: list[Any] | None = None

class VideoAddToAlbum(VKMethod[Any]):
    __api_method__ = 'video.addToAlbum'
    target_id: int | None = None
    album_id: int | None = None
    album_ids: list[Any] | None = None
    owner_id: int = ...
    video_id: int = ...

class VideoCreateComment(VKMethod[Any]):
    __api_method__ = 'video.createComment'
    owner_id: int | None = None
    video_id: int = ...
    message: str | None = None
    attachments: list[Any] | None = None
    from_group: bool | None = None
    reply_to_comment: int | None = None
    sticker_id: int | None = None
    guid: str | None = None
    track_code: str | None = None

class VideoDelete(VKMethod[Any]):
    __api_method__ = 'video.delete'
    video_id: int = ...
    owner_id: int | None = None
    target_id: int | None = None

class VideoDeleteAlbum(VKMethod[Any]):
    __api_method__ = 'video.deleteAlbum'
    group_id: int | None = None
    album_id: int = ...
    owner_id: int | None = None

class VideoDeleteComment(VKMethod[Any]):
    __api_method__ = 'video.deleteComment'
    owner_id: int | None = None
    comment_id: int = ...

class VideoDeleteThread(VKMethod[Any]):
    __api_method__ = 'video.deleteThread'
    owner_id: int = ...
    thread_id: int = ...

class VideoEdit(VKMethod[Any]):
    __api_method__ = 'video.edit'
    owner_id: int | None = None
    video_id: int = ...
    name: str | None = None
    desc: str | None = None
    privacy_view: list[Any] | None = None
    privacy_comment: list[Any] | None = None
    no_comments: bool | None = None
    repeat: bool | None = None
    ord_info: str | None = None

class VideoEditAlbum(VKMethod[Any]):
    __api_method__ = 'video.editAlbum'
    group_id: int | None = None
    album_id: int = ...
    title: str | None = None
    privacy: list[Any] | None = None
    owner_id: int | None = None

class VideoEditComment(VKMethod[Any]):
    __api_method__ = 'video.editComment'
    owner_id: int | None = None
    comment_id: int = ...
    message: str | None = None
    attachments: list[Any] | None = None

class VideoGet(VKMethod[Any]):
    __api_method__ = 'video.get'
    owner_id: int | None = None
    videos: list[Any] | None = None
    album_id: int | None = None
    count: int | None = None
    offset: int | None = None
    extended: bool | None = None
    fields: list[Any] | None = None
    sort_album: int | None = None

class VideoGetAlbumById(VKMethod[Any]):
    __api_method__ = 'video.getAlbumById'
    owner_id: int | None = None
    album_id: int = ...

class VideoGetAlbums(VKMethod[Any]):
    __api_method__ = 'video.getAlbums'
    owner_id: int | None = None
    offset: int | None = None
    count: int | None = None
    extended: bool | None = None
    need_system: bool | None = None

class VideoGetAlbumsByVideo(VKMethod[Any]):
    __api_method__ = 'video.getAlbumsByVideo'
    target_id: int | None = None
    owner_id: int = ...
    video_id: int = ...
    extended: bool | None = None

class VideoGetComments(VKMethod[Any]):
    __api_method__ = 'video.getComments'
    owner_id: int | None = None
    video_id: int = ...
    need_likes: bool | None = None
    start_comment_id: int | None = None
    offset: int | None = None
    count: int | None = None
    sort: str | None = None
    extended: bool | None = None
    fields: list[Any] | None = None
    comment_id: int | None = None
    thread_items_count: int | None = None

class VideoGetLongPollServer(VKMethod[Any]):
    __api_method__ = 'video.getLongPollServer'
    owner_id: int | None = None
    video_id: int = ...

class VideoGetOembed(VKMethod[Any]):
    __api_method__ = 'video.getOembed'
    url: str = ...
    maxwidth: int | None = None
    maxheight: int | None = None

class VideoGetThumbUploadUrl(VKMethod[Any]):
    __api_method__ = 'video.getThumbUploadUrl'
    owner_id: int = ...

class VideoLiveGetCategories(VKMethod[Any]):
    __api_method__ = 'video.liveGetCategories'
    pass

class VideoRemoveFromAlbum(VKMethod[Any]):
    __api_method__ = 'video.removeFromAlbum'
    target_id: int | None = None
    album_id: int | None = None
    album_ids: list[Any] | None = None
    owner_id: int = ...
    video_id: int = ...

class VideoReorderAlbums(VKMethod[Any]):
    __api_method__ = 'video.reorderAlbums'
    owner_id: int | None = None
    album_id: int = ...
    before: int | None = None
    after: int | None = None

class VideoReorderVideos(VKMethod[Any]):
    __api_method__ = 'video.reorderVideos'
    target_id: int | None = None
    album_id: int | None = None
    owner_id: int = ...
    video_id: int = ...
    before_owner_id: int | None = None
    before_video_id: int | None = None
    after_owner_id: int | None = None
    after_video_id: int | None = None

class VideoReport(VKMethod[Any]):
    __api_method__ = 'video.report'
    owner_id: int = ...
    video_id: int = ...
    reason: int | None = None
    comment: str | None = None
    search_query: str | None = None

class VideoReportComment(VKMethod[Any]):
    __api_method__ = 'video.reportComment'
    owner_id: int = ...
    comment_id: int = ...
    reason: int | None = None

class VideoRestore(VKMethod[Any]):
    __api_method__ = 'video.restore'
    video_id: int = ...
    owner_id: int | None = None

class VideoRestoreComment(VKMethod[Any]):
    __api_method__ = 'video.restoreComment'
    owner_id: int | None = None
    comment_id: int = ...

class VideoRestoreThread(VKMethod[Any]):
    __api_method__ = 'video.restoreThread'
    owner_id: int = ...
    thread_id: int = ...

class VideoSave(VKMethod[Any]):
    __api_method__ = 'video.save'
    name: str | None = None
    description: str | None = None
    is_private: bool | None = None
    wallpost: bool | None = None
    link: str | None = None
    group_id: int | None = None
    album_id: int | None = None
    privacy_view: list[Any] | None = None
    privacy_comment: list[Any] | None = None
    no_comments: bool | None = None
    repeat: bool | None = None
    compression: bool | None = None
    ord_info: str | None = None
    auto_publish: bool | None = None

class VideoSaveUploadedThumb(VKMethod[Any]):
    __api_method__ = 'video.saveUploadedThumb'
    owner_id: int = ...
    thumb_json: str = ...
    thumb_size: str | None = None
    random_tag: str | None = None
    video_id: int | None = None
    set_thumb: bool | None = None

class VideoSearch(VKMethod[Any]):
    __api_method__ = 'video.search'
    q: str | None = None
    sort: int | None = None
    hd: int | None = None
    adult: bool | None = None
    live: bool | None = None
    filters: list[Any] | None = None
    search_own: bool | None = None
    offset: int | None = None
    longer: int | None = None
    shorter: int | None = None
    count: int | None = None
    extended: bool | None = None
    owner_id: int | None = None
    fields: list[Any] | None = None

class VideoStartStreaming(VKMethod[Any]):
    __api_method__ = 'video.startStreaming'
    video_id: int | None = None
    name: str | None = None
    description: str | None = None
    wallpost: bool | None = None
    group_id: int | None = None
    privacy_view: list[Any] | None = None
    privacy_comment: list[Any] | None = None
    no_comments: bool | None = None
    category_id: int | None = None
    publish: bool | None = None

class VideoStopStreaming(VKMethod[Any]):
    __api_method__ = 'video.stopStreaming'
    group_id: int | None = None
    video_id: int | None = None

class VideoUnpinComment(VKMethod[Any]):
    __api_method__ = 'video.unpinComment'
    owner_id: int = ...
    comment_id: int = ...

class WallCheckCopyrightLink(VKMethod[Any]):
    __api_method__ = 'wall.checkCopyrightLink'
    link: str = ...

class WallCloseComments(VKMethod[Any]):
    __api_method__ = 'wall.closeComments'
    owner_id: int = ...
    post_id: int = ...

class WallCreateComment(VKMethod[Any]):
    __api_method__ = 'wall.createComment'
    owner_id: int | None = None
    post_id: int = ...
    from_group: int | None = None
    message: str | None = None
    reply_to_comment: int | None = None
    attachments: list[Any] | None = None
    sticker_id: int | None = None
    guid: str | None = None

class WallDelete(VKMethod[Any]):
    __api_method__ = 'wall.delete'
    owner_id: int | None = None
    post_id: int | None = None

class WallDeleteComment(VKMethod[Any]):
    __api_method__ = 'wall.deleteComment'
    owner_id: int | None = None
    post_id: int | None = None
    comment_id: int = ...

class WallEdit(VKMethod[Any]):
    __api_method__ = 'wall.edit'
    owner_id: int | None = None
    post_id: int = ...
    friends_only: bool | None = None
    message: str | None = None
    attachments: list[Any] | None = None
    services: str | None = None
    signed: bool | None = None
    publish_date: int | None = None
    lat: float | None = None
    long: float | None = None
    place_id: int | None = None
    mark_as_ads: bool | None = None
    close_comments: bool | None = None
    donut_paid_duration: int | None = None
    poster_bkg_id: int | None = None
    poster_bkg_owner_id: int | None = None
    poster_bkg_access_hash: str | None = None
    copyright: str | None = None
    topic_id: int | None = None

class WallEditAdsStealth(VKMethod[Any]):
    __api_method__ = 'wall.editAdsStealth'
    owner_id: int | None = None
    post_id: int = ...
    message: str | None = None
    attachments: list[Any] | None = None
    signed: bool | None = None
    lat: float | None = None
    long: float | None = None
    place_id: int | None = None
    link_button: str | None = None
    link_title: str | None = None
    link_image: str | None = None
    link_video: str | None = None

class WallEditComment(VKMethod[Any]):
    __api_method__ = 'wall.editComment'
    owner_id: int | None = None
    post_id: int | None = None
    comment_id: int = ...
    message: str | None = None
    attachments: list[Any] | None = None

class WallGet(VKMethod[Any]):
    __api_method__ = 'wall.get'
    domain: int | str | None = None
    offset: int | None = None
    count: int | None = None
    filter: str | None = None
    extended: bool | None = None
    fields: list[Any] | None = None

class WallGetById(VKMethod[Any]):
    __api_method__ = 'wall.getById'
    posts: list[Any] = ...
    extended: bool | None = None
    copy_history_depth: int | None = None
    fields: list[Any] | None = None

class WallGetComment(VKMethod[Any]):
    __api_method__ = 'wall.getComment'
    owner_id: int | None = None
    comment_id: int = ...
    extended: bool | None = None
    fields: list[Any] | None = None

class WallGetComments(VKMethod[Any]):
    __api_method__ = 'wall.getComments'
    owner_id: int | None = None
    post_id: int | None = None
    need_likes: bool | None = None
    start_comment_id: int | None = None
    offset: int | None = None
    count: int | None = None
    sort: str | None = None
    preview_length: int | None = None
    extended: bool | None = None
    fields: list[Any] | None = None
    comment_id: int | None = None
    thread_items_count: int | None = None

class WallGetReposts(VKMethod[Any]):
    __api_method__ = 'wall.getReposts'
    owner_id: int | None = None
    post_id: int | None = None
    offset: int | None = None
    count: int | None = None

class WallOpenComments(VKMethod[Any]):
    __api_method__ = 'wall.openComments'
    owner_id: int = ...
    post_id: int = ...

class WallParseAttachedLink(VKMethod[Any]):
    __api_method__ = 'wall.parseAttachedLink'
    links: str = ...
    extended: bool | None = None
    fields: list[Any] | None = None
    name_case: str | None = None

class WallPin(VKMethod[Any]):
    __api_method__ = 'wall.pin'
    owner_id: int | None = None
    post_id: int = ...

class WallPost(VKMethod[Any]):
    __api_method__ = 'wall.post'
    owner_id: int | None = None
    friends_only: bool | None = None
    from_group: bool | None = None
    message: str | None = None
    attachments: list[Any] | None = None
    services: str | None = None
    signed: bool | None = None
    publish_date: int | None = None
    lat: float | None = None
    long: float | None = None
    place_id: int | None = None
    post_id: int | None = None
    guid: str | None = None
    mark_as_ads: bool | None = None
    link_title: str | None = None
    link_photo_id: str | None = None
    close_comments: bool | None = None
    donut_paid_duration: int | None = None
    mute_notifications: bool | None = None
    copyright: str | None = None

class WallPostAdsStealth(VKMethod[Any]):
    __api_method__ = 'wall.postAdsStealth'
    owner_id: int = ...
    message: str | None = None
    attachments: list[Any] | None = None
    signed: bool | None = None
    lat: float | None = None
    long: float | None = None
    place_id: int | None = None
    guid: str | None = None
    link_button: str | None = None
    link_title: str | None = None
    link_image: str | None = None
    link_video: str | None = None

class WallReportComment(VKMethod[Any]):
    __api_method__ = 'wall.reportComment'
    owner_id: int = ...
    comment_id: int = ...
    reason: int = ...

class WallReportPost(VKMethod[Any]):
    __api_method__ = 'wall.reportPost'
    owner_id: int = ...
    post_id: int = ...
    reason: int = ...

class WallRepost(VKMethod[Any]):
    __api_method__ = 'wall.repost'
    object: str = ...
    message: str | None = None
    group_id: int | None = None
    mark_as_ads: bool | None = None
    mute_notifications: bool | None = None

class WallRestore(VKMethod[Any]):
    __api_method__ = 'wall.restore'
    owner_id: int | None = None
    post_id: int | None = None

class WallRestoreComment(VKMethod[Any]):
    __api_method__ = 'wall.restoreComment'
    owner_id: int | None = None
    comment_id: int = ...

class WallSearch(VKMethod[Any]):
    __api_method__ = 'wall.search'
    domain: int | str | None = None
    query: str | None = None
    owners_only: bool | None = None
    count: int | None = None
    offset: int | None = None
    extended: bool | None = None
    fields: list[Any] | None = None

class WallUnpin(VKMethod[Any]):
    __api_method__ = 'wall.unpin'
    owner_id: int | None = None
    post_id: int = ...

class WidgetsGetComments(VKMethod[Any]):
    __api_method__ = 'widgets.getComments'
    widget_api_id: int | None = None
    url: str | None = None
    page_id: str | None = None
    order: str | None = None
    fields: list[Any] | None = None
    offset: int | None = None
    count: int | None = None

class WidgetsGetPages(VKMethod[Any]):
    __api_method__ = 'widgets.getPages'
    widget_api_id: int | None = None
    order: str | None = None
    period: str | None = None
    offset: int | None = None
    count: int | None = None

class AccountMethods(MethodNamespace):
    async def ban(self, **params: Any) -> Any:
        return await self._bot(AccountBan(**params))

    async def change_password(self, **params: Any) -> Any:
        return await self._bot(AccountChangePassword(**params))

    async def get_active_offers(self, **params: Any) -> Any:
        return await self._bot(AccountGetActiveOffers(**params))

    async def get_app_permissions(self, **params: Any) -> Any:
        return await self._bot(AccountGetAppPermissions(**params))

    async def get_banned(self, **params: Any) -> Any:
        return await self._bot(AccountGetBanned(**params))

    async def get_counters(self, **params: Any) -> Any:
        return await self._bot(AccountGetCounters(**params))

    async def get_info(self, **params: Any) -> Any:
        return await self._bot(AccountGetInfo(**params))

    async def get_profile_info(self, **params: Any) -> Any:
        return await self._bot(AccountGetProfileInfo(**params))

    async def get_push_settings(self, **params: Any) -> Any:
        return await self._bot(AccountGetPushSettings(**params))

    async def register_device(self, **params: Any) -> Any:
        return await self._bot(AccountRegisterDevice(**params))

    async def save_profile_info(self, **params: Any) -> Any:
        return await self._bot(AccountSaveProfileInfo(**params))

    async def set_info(self, **params: Any) -> Any:
        return await self._bot(AccountSetInfo(**params))

    async def set_offline(self, **params: Any) -> Any:
        return await self._bot(AccountSetOffline(**params))

    async def set_online(self, **params: Any) -> Any:
        return await self._bot(AccountSetOnline(**params))

    async def set_push_settings(self, **params: Any) -> Any:
        return await self._bot(AccountSetPushSettings(**params))

    async def set_silence_mode(self, **params: Any) -> Any:
        return await self._bot(AccountSetSilenceMode(**params))

    async def unban(self, **params: Any) -> Any:
        return await self._bot(AccountUnban(**params))

    async def unregister_device(self, **params: Any) -> Any:
        return await self._bot(AccountUnregisterDevice(**params))


class AdsMethods(MethodNamespace):
    async def add_office_users(self, **params: Any) -> Any:
        return await self._bot(AdsAddOfficeUsers(**params))

    async def check_link(self, **params: Any) -> Any:
        return await self._bot(AdsCheckLink(**params))

    async def create_ads(self, **params: Any) -> Any:
        return await self._bot(AdsCreateAds(**params))

    async def create_campaigns(self, **params: Any) -> Any:
        return await self._bot(AdsCreateCampaigns(**params))

    async def create_clients(self, **params: Any) -> Any:
        return await self._bot(AdsCreateClients(**params))

    async def create_lookalike_request(self, **params: Any) -> Any:
        return await self._bot(AdsCreateLookalikeRequest(**params))

    async def create_target_group(self, **params: Any) -> Any:
        return await self._bot(AdsCreateTargetGroup(**params))

    async def create_target_pixel(self, **params: Any) -> Any:
        return await self._bot(AdsCreateTargetPixel(**params))

    async def delete_ads(self, **params: Any) -> Any:
        return await self._bot(AdsDeleteAds(**params))

    async def delete_campaigns(self, **params: Any) -> Any:
        return await self._bot(AdsDeleteCampaigns(**params))

    async def delete_clients(self, **params: Any) -> Any:
        return await self._bot(AdsDeleteClients(**params))

    async def delete_target_group(self, **params: Any) -> Any:
        return await self._bot(AdsDeleteTargetGroup(**params))

    async def delete_target_pixel(self, **params: Any) -> Any:
        return await self._bot(AdsDeleteTargetPixel(**params))

    async def get_accounts(self, **params: Any) -> Any:
        return await self._bot(AdsGetAccounts(**params))

    async def get_ads(self, **params: Any) -> Any:
        return await self._bot(AdsGetAds(**params))

    async def get_ads_layout(self, **params: Any) -> Any:
        return await self._bot(AdsGetAdsLayout(**params))

    async def get_ads_targeting(self, **params: Any) -> Any:
        return await self._bot(AdsGetAdsTargeting(**params))

    async def get_budget(self, **params: Any) -> Any:
        return await self._bot(AdsGetBudget(**params))

    async def get_campaigns(self, **params: Any) -> Any:
        return await self._bot(AdsGetCampaigns(**params))

    async def get_categories(self, **params: Any) -> Any:
        return await self._bot(AdsGetCategories(**params))

    async def get_clients(self, **params: Any) -> Any:
        return await self._bot(AdsGetClients(**params))

    async def get_demographics(self, **params: Any) -> Any:
        return await self._bot(AdsGetDemographics(**params))

    async def get_flood_stats(self, **params: Any) -> Any:
        return await self._bot(AdsGetFloodStats(**params))

    async def get_lookalike_requests(self, **params: Any) -> Any:
        return await self._bot(AdsGetLookalikeRequests(**params))

    async def get_musicians(self, **params: Any) -> Any:
        return await self._bot(AdsGetMusicians(**params))

    async def get_musicians_by_ids(self, **params: Any) -> Any:
        return await self._bot(AdsGetMusiciansByIds(**params))

    async def get_office_users(self, **params: Any) -> Any:
        return await self._bot(AdsGetOfficeUsers(**params))

    async def get_posts_reach(self, **params: Any) -> Any:
        return await self._bot(AdsGetPostsReach(**params))

    async def get_rejection_reason(self, **params: Any) -> Any:
        return await self._bot(AdsGetRejectionReason(**params))

    async def get_statistics(self, **params: Any) -> Any:
        return await self._bot(AdsGetStatistics(**params))

    async def get_suggestions(self, **params: Any) -> Any:
        return await self._bot(AdsGetSuggestions(**params))

    async def get_target_groups(self, **params: Any) -> Any:
        return await self._bot(AdsGetTargetGroups(**params))

    async def get_target_pixels(self, **params: Any) -> Any:
        return await self._bot(AdsGetTargetPixels(**params))

    async def get_targeting_stats(self, **params: Any) -> Any:
        return await self._bot(AdsGetTargetingStats(**params))

    async def get_upload_u_r_l(self, **params: Any) -> Any:
        return await self._bot(AdsGetUploadURL(**params))

    async def get_video_upload_u_r_l(self, **params: Any) -> Any:
        return await self._bot(AdsGetVideoUploadURL(**params))

    async def import_target_contacts(self, **params: Any) -> Any:
        return await self._bot(AdsImportTargetContacts(**params))

    async def remove_office_users(self, **params: Any) -> Any:
        return await self._bot(AdsRemoveOfficeUsers(**params))

    async def remove_target_contacts(self, **params: Any) -> Any:
        return await self._bot(AdsRemoveTargetContacts(**params))

    async def save_lookalike_request_result(self, **params: Any) -> Any:
        return await self._bot(AdsSaveLookalikeRequestResult(**params))

    async def share_target_group(self, **params: Any) -> Any:
        return await self._bot(AdsShareTargetGroup(**params))

    async def update_ads(self, **params: Any) -> Any:
        return await self._bot(AdsUpdateAds(**params))

    async def update_campaigns(self, **params: Any) -> Any:
        return await self._bot(AdsUpdateCampaigns(**params))

    async def update_clients(self, **params: Any) -> Any:
        return await self._bot(AdsUpdateClients(**params))

    async def update_office_users(self, **params: Any) -> Any:
        return await self._bot(AdsUpdateOfficeUsers(**params))

    async def update_target_group(self, **params: Any) -> Any:
        return await self._bot(AdsUpdateTargetGroup(**params))

    async def update_target_pixel(self, **params: Any) -> Any:
        return await self._bot(AdsUpdateTargetPixel(**params))


class ApiMethods(MethodNamespace):
    async def execute(self, **params: Any) -> Any:
        return await self._bot(Execute(**params))


class AppWidgetsMethods(MethodNamespace):
    async def get_app_image_upload_server(self, **params: Any) -> Any:
        return await self._bot(AppWidgetsGetAppImageUploadServer(**params))

    async def get_app_images(self, **params: Any) -> Any:
        return await self._bot(AppWidgetsGetAppImages(**params))

    async def get_group_image_upload_server(self, **params: Any) -> Any:
        return await self._bot(AppWidgetsGetGroupImageUploadServer(**params))

    async def get_group_images(self, **params: Any) -> Any:
        return await self._bot(AppWidgetsGetGroupImages(**params))

    async def get_images_by_id(self, **params: Any) -> Any:
        return await self._bot(AppWidgetsGetImagesById(**params))

    async def save_app_image(self, **params: Any) -> Any:
        return await self._bot(AppWidgetsSaveAppImage(**params))

    async def save_group_image(self, **params: Any) -> Any:
        return await self._bot(AppWidgetsSaveGroupImage(**params))

    async def update(self, **params: Any) -> Any:
        return await self._bot(AppWidgetsUpdate(**params))


class AppsMethods(MethodNamespace):
    async def add_snippet(self, **params: Any) -> Any:
        return await self._bot(AppsAddSnippet(**params))

    async def add_users_to_testing_group(self, **params: Any) -> Any:
        return await self._bot(AppsAddUsersToTestingGroup(**params))

    async def delete_app_requests(self, **params: Any) -> Any:
        return await self._bot(AppsDeleteAppRequests(**params))

    async def delete_snippet(self, **params: Any) -> Any:
        return await self._bot(AppsDeleteSnippet(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(AppsGet(**params))

    async def get_catalog(self, **params: Any) -> Any:
        return await self._bot(AppsGetCatalog(**params))

    async def get_friends_list(self, **params: Any) -> Any:
        return await self._bot(AppsGetFriendsList(**params))

    async def get_leaderboard(self, **params: Any) -> Any:
        return await self._bot(AppsGetLeaderboard(**params))

    async def get_mini_app_policies(self, **params: Any) -> Any:
        return await self._bot(AppsGetMiniAppPolicies(**params))

    async def get_scopes(self, **params: Any) -> Any:
        return await self._bot(AppsGetScopes(**params))

    async def get_score(self, **params: Any) -> Any:
        return await self._bot(AppsGetScore(**params))

    async def get_snippets(self, **params: Any) -> Any:
        return await self._bot(AppsGetSnippets(**params))

    async def get_testing_groups(self, **params: Any) -> Any:
        return await self._bot(AppsGetTestingGroups(**params))

    async def is_notifications_allowed(self, **params: Any) -> Any:
        return await self._bot(AppsIsNotificationsAllowed(**params))

    async def promo_has_active_gift(self, **params: Any) -> Any:
        return await self._bot(AppsPromoHasActiveGift(**params))

    async def promo_use_gift(self, **params: Any) -> Any:
        return await self._bot(AppsPromoUseGift(**params))

    async def remove_testing_group(self, **params: Any) -> Any:
        return await self._bot(AppsRemoveTestingGroup(**params))

    async def remove_users_from_testing_groups(self, **params: Any) -> Any:
        return await self._bot(AppsRemoveUsersFromTestingGroups(**params))

    async def send_request(self, **params: Any) -> Any:
        return await self._bot(AppsSendRequest(**params))

    async def update_meta_for_testing_group(self, **params: Any) -> Any:
        return await self._bot(AppsUpdateMetaForTestingGroup(**params))


class AuthMethods(MethodNamespace):
    async def restore(self, **params: Any) -> Any:
        return await self._bot(AuthRestore(**params))


class BoardMethods(MethodNamespace):
    async def add_topic(self, **params: Any) -> Any:
        return await self._bot(BoardAddTopic(**params))

    async def close_topic(self, **params: Any) -> Any:
        return await self._bot(BoardCloseTopic(**params))

    async def create_comment(self, **params: Any) -> Any:
        return await self._bot(BoardCreateComment(**params))

    async def delete_comment(self, **params: Any) -> Any:
        return await self._bot(BoardDeleteComment(**params))

    async def delete_topic(self, **params: Any) -> Any:
        return await self._bot(BoardDeleteTopic(**params))

    async def edit_comment(self, **params: Any) -> Any:
        return await self._bot(BoardEditComment(**params))

    async def edit_topic(self, **params: Any) -> Any:
        return await self._bot(BoardEditTopic(**params))

    async def fix_topic(self, **params: Any) -> Any:
        return await self._bot(BoardFixTopic(**params))

    async def get_comments(self, **params: Any) -> Any:
        return await self._bot(BoardGetComments(**params))

    async def get_topics(self, **params: Any) -> Any:
        return await self._bot(BoardGetTopics(**params))

    async def open_topic(self, **params: Any) -> Any:
        return await self._bot(BoardOpenTopic(**params))

    async def restore_comment(self, **params: Any) -> Any:
        return await self._bot(BoardRestoreComment(**params))

    async def unfix_topic(self, **params: Any) -> Any:
        return await self._bot(BoardUnfixTopic(**params))


class BugtrackerMethods(MethodNamespace):
    async def add_company_groups_members(self, **params: Any) -> Any:
        return await self._bot(BugtrackerAddCompanyGroupsMembers(**params))

    async def add_company_members(self, **params: Any) -> Any:
        return await self._bot(BugtrackerAddCompanyMembers(**params))

    async def change_bugreport_status(self, **params: Any) -> Any:
        return await self._bot(BugtrackerChangeBugreportStatus(**params))

    async def create_comment(self, **params: Any) -> Any:
        return await self._bot(BugtrackerCreateComment(**params))

    async def get_bugreport_by_id(self, **params: Any) -> Any:
        return await self._bot(BugtrackerGetBugreportById(**params))

    async def get_company_group_members(self, **params: Any) -> Any:
        return await self._bot(BugtrackerGetCompanyGroupMembers(**params))

    async def get_company_members(self, **params: Any) -> Any:
        return await self._bot(BugtrackerGetCompanyMembers(**params))

    async def get_download_version_url(self, **params: Any) -> Any:
        return await self._bot(BugtrackerGetDownloadVersionUrl(**params))

    async def get_product_build_upload_server(self, **params: Any) -> Any:
        return await self._bot(BugtrackerGetProductBuildUploadServer(**params))

    async def remove_company_group_member(self, **params: Any) -> Any:
        return await self._bot(BugtrackerRemoveCompanyGroupMember(**params))

    async def remove_company_member(self, **params: Any) -> Any:
        return await self._bot(BugtrackerRemoveCompanyMember(**params))

    async def save_product_version(self, **params: Any) -> Any:
        return await self._bot(BugtrackerSaveProductVersion(**params))

    async def set_company_member_role(self, **params: Any) -> Any:
        return await self._bot(BugtrackerSetCompanyMemberRole(**params))

    async def set_product_is_over(self, **params: Any) -> Any:
        return await self._bot(BugtrackerSetProductIsOver(**params))


class CallsMethods(MethodNamespace):
    async def force_finish(self, **params: Any) -> Any:
        return await self._bot(CallsForceFinish(**params))

    async def start(self, **params: Any) -> Any:
        return await self._bot(CallsStart(**params))


class DatabaseMethods(MethodNamespace):
    async def get_chairs(self, **params: Any) -> Any:
        return await self._bot(DatabaseGetChairs(**params))

    async def get_cities(self, **params: Any) -> Any:
        return await self._bot(DatabaseGetCities(**params))

    async def get_cities_by_id(self, **params: Any) -> Any:
        return await self._bot(DatabaseGetCitiesById(**params))

    async def get_countries(self, **params: Any) -> Any:
        return await self._bot(DatabaseGetCountries(**params))

    async def get_countries_by_id(self, **params: Any) -> Any:
        return await self._bot(DatabaseGetCountriesById(**params))

    async def get_faculties(self, **params: Any) -> Any:
        return await self._bot(DatabaseGetFaculties(**params))

    async def get_metro_stations(self, **params: Any) -> Any:
        return await self._bot(DatabaseGetMetroStations(**params))

    async def get_metro_stations_by_id(self, **params: Any) -> Any:
        return await self._bot(DatabaseGetMetroStationsById(**params))

    async def get_regions(self, **params: Any) -> Any:
        return await self._bot(DatabaseGetRegions(**params))

    async def get_school_classes(self, **params: Any) -> Any:
        return await self._bot(DatabaseGetSchoolClasses(**params))

    async def get_schools(self, **params: Any) -> Any:
        return await self._bot(DatabaseGetSchools(**params))

    async def get_universities(self, **params: Any) -> Any:
        return await self._bot(DatabaseGetUniversities(**params))


class DocsMethods(MethodNamespace):
    async def add(self, **params: Any) -> Any:
        return await self._bot(DocsAdd(**params))

    async def delete(self, **params: Any) -> Any:
        return await self._bot(DocsDelete(**params))

    async def edit(self, **params: Any) -> Any:
        return await self._bot(DocsEdit(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(DocsGet(**params))

    async def get_by_id(self, **params: Any) -> Any:
        return await self._bot(DocsGetById(**params))

    async def get_messages_upload_server(self, **params: Any) -> Any:
        return await self._bot(DocsGetMessagesUploadServer(**params))

    async def get_types(self, **params: Any) -> Any:
        return await self._bot(DocsGetTypes(**params))

    async def get_upload_server(self, **params: Any) -> Any:
        return await self._bot(DocsGetUploadServer(**params))

    async def get_wall_upload_server(self, **params: Any) -> Any:
        return await self._bot(DocsGetWallUploadServer(**params))

    async def restore(self, **params: Any) -> Any:
        return await self._bot(DocsRestore(**params))

    async def save(self, **params: Any) -> Any:
        return await self._bot(DocsSave(**params))

    async def search(self, **params: Any) -> Any:
        return await self._bot(DocsSearch(**params))


class DonutMethods(MethodNamespace):
    async def get_friends(self, **params: Any) -> Any:
        return await self._bot(DonutGetFriends(**params))

    async def get_subscription(self, **params: Any) -> Any:
        return await self._bot(DonutGetSubscription(**params))

    async def get_subscriptions(self, **params: Any) -> Any:
        return await self._bot(DonutGetSubscriptions(**params))

    async def is_don(self, **params: Any) -> Any:
        return await self._bot(DonutIsDon(**params))


class DownloadedGamesMethods(MethodNamespace):
    async def get_paid_status(self, **params: Any) -> Any:
        return await self._bot(DownloadedGamesGetPaidStatus(**params))


class FaveMethods(MethodNamespace):
    async def add_article(self, **params: Any) -> Any:
        return await self._bot(FaveAddArticle(**params))

    async def add_link(self, **params: Any) -> Any:
        return await self._bot(FaveAddLink(**params))

    async def add_page(self, **params: Any) -> Any:
        return await self._bot(FaveAddPage(**params))

    async def add_post(self, **params: Any) -> Any:
        return await self._bot(FaveAddPost(**params))

    async def add_product(self, **params: Any) -> Any:
        return await self._bot(FaveAddProduct(**params))

    async def add_tag(self, **params: Any) -> Any:
        return await self._bot(FaveAddTag(**params))

    async def add_video(self, **params: Any) -> Any:
        return await self._bot(FaveAddVideo(**params))

    async def edit_tag(self, **params: Any) -> Any:
        return await self._bot(FaveEditTag(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(FaveGet(**params))

    async def get_pages(self, **params: Any) -> Any:
        return await self._bot(FaveGetPages(**params))

    async def get_tags(self, **params: Any) -> Any:
        return await self._bot(FaveGetTags(**params))

    async def mark_seen(self, **params: Any) -> Any:
        return await self._bot(FaveMarkSeen(**params))

    async def remove_article(self, **params: Any) -> Any:
        return await self._bot(FaveRemoveArticle(**params))

    async def remove_link(self, **params: Any) -> Any:
        return await self._bot(FaveRemoveLink(**params))

    async def remove_page(self, **params: Any) -> Any:
        return await self._bot(FaveRemovePage(**params))

    async def remove_post(self, **params: Any) -> Any:
        return await self._bot(FaveRemovePost(**params))

    async def remove_product(self, **params: Any) -> Any:
        return await self._bot(FaveRemoveProduct(**params))

    async def remove_tag(self, **params: Any) -> Any:
        return await self._bot(FaveRemoveTag(**params))

    async def remove_video(self, **params: Any) -> Any:
        return await self._bot(FaveRemoveVideo(**params))

    async def reorder_tags(self, **params: Any) -> Any:
        return await self._bot(FaveReorderTags(**params))

    async def set_page_tags(self, **params: Any) -> Any:
        return await self._bot(FaveSetPageTags(**params))

    async def set_tags(self, **params: Any) -> Any:
        return await self._bot(FaveSetTags(**params))

    async def track_page_interaction(self, **params: Any) -> Any:
        return await self._bot(FaveTrackPageInteraction(**params))


class FriendsMethods(MethodNamespace):
    async def add(self, **params: Any) -> Any:
        return await self._bot(FriendsAdd(**params))

    async def add_list(self, **params: Any) -> Any:
        return await self._bot(FriendsAddList(**params))

    async def are_friends(self, **params: Any) -> Any:
        return await self._bot(FriendsAreFriends(**params))

    async def delete(self, **params: Any) -> Any:
        return await self._bot(FriendsDelete(**params))

    async def delete_all_requests(self, **params: Any) -> Any:
        return await self._bot(FriendsDeleteAllRequests(**params))

    async def delete_list(self, **params: Any) -> Any:
        return await self._bot(FriendsDeleteList(**params))

    async def edit(self, **params: Any) -> Any:
        return await self._bot(FriendsEdit(**params))

    async def edit_list(self, **params: Any) -> Any:
        return await self._bot(FriendsEditList(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(FriendsGet(**params))

    async def get_app_users(self, **params: Any) -> Any:
        return await self._bot(FriendsGetAppUsers(**params))

    async def get_lists(self, **params: Any) -> Any:
        return await self._bot(FriendsGetLists(**params))

    async def get_mutual(self, **params: Any) -> Any:
        return await self._bot(FriendsGetMutual(**params))

    async def get_online(self, **params: Any) -> Any:
        return await self._bot(FriendsGetOnline(**params))

    async def get_recent(self, **params: Any) -> Any:
        return await self._bot(FriendsGetRecent(**params))

    async def get_requests(self, **params: Any) -> Any:
        return await self._bot(FriendsGetRequests(**params))

    async def get_suggestions(self, **params: Any) -> Any:
        return await self._bot(FriendsGetSuggestions(**params))

    async def search(self, **params: Any) -> Any:
        return await self._bot(FriendsSearch(**params))


class GiftsMethods(MethodNamespace):
    async def get(self, **params: Any) -> Any:
        return await self._bot(GiftsGet(**params))


class GroupsMethods(MethodNamespace):
    async def add_address(self, **params: Any) -> Any:
        return await self._bot(GroupsAddAddress(**params))

    async def add_callback_server(self, **params: Any) -> Any:
        return await self._bot(GroupsAddCallbackServer(**params))

    async def add_link(self, **params: Any) -> Any:
        return await self._bot(GroupsAddLink(**params))

    async def approve_request(self, **params: Any) -> Any:
        return await self._bot(GroupsApproveRequest(**params))

    async def ban(self, **params: Any) -> Any:
        return await self._bot(GroupsBan(**params))

    async def create(self, **params: Any) -> Any:
        return await self._bot(GroupsCreate(**params))

    async def delete_address(self, **params: Any) -> Any:
        return await self._bot(GroupsDeleteAddress(**params))

    async def delete_callback_server(self, **params: Any) -> Any:
        return await self._bot(GroupsDeleteCallbackServer(**params))

    async def delete_link(self, **params: Any) -> Any:
        return await self._bot(GroupsDeleteLink(**params))

    async def disable_online(self, **params: Any) -> Any:
        return await self._bot(GroupsDisableOnline(**params))

    async def edit(self, **params: Any) -> Any:
        return await self._bot(GroupsEdit(**params))

    async def edit_address(self, **params: Any) -> Any:
        return await self._bot(GroupsEditAddress(**params))

    async def edit_callback_server(self, **params: Any) -> Any:
        return await self._bot(GroupsEditCallbackServer(**params))

    async def edit_link(self, **params: Any) -> Any:
        return await self._bot(GroupsEditLink(**params))

    async def edit_manager(self, **params: Any) -> Any:
        return await self._bot(GroupsEditManager(**params))

    async def enable_online(self, **params: Any) -> Any:
        return await self._bot(GroupsEnableOnline(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(GroupsGet(**params))

    async def get_addresses(self, **params: Any) -> Any:
        return await self._bot(GroupsGetAddresses(**params))

    async def get_banned(self, **params: Any) -> Any:
        return await self._bot(GroupsGetBanned(**params))

    async def get_by_id(self, **params: Any) -> Any:
        return await self._bot(GroupsGetById(**params))

    async def get_callback_confirmation_code(self, **params: Any) -> Any:
        return await self._bot(GroupsGetCallbackConfirmationCode(**params))

    async def get_callback_servers(self, **params: Any) -> Any:
        return await self._bot(GroupsGetCallbackServers(**params))

    async def get_callback_settings(self, **params: Any) -> Any:
        return await self._bot(GroupsGetCallbackSettings(**params))

    async def get_catalog_info(self, **params: Any) -> Any:
        return await self._bot(GroupsGetCatalogInfo(**params))

    async def get_invited_users(self, **params: Any) -> Any:
        return await self._bot(GroupsGetInvitedUsers(**params))

    async def get_invites(self, **params: Any) -> Any:
        return await self._bot(GroupsGetInvites(**params))

    async def get_long_poll_server(self, **params: Any) -> Any:
        return await self._bot(GroupsGetLongPollServer(**params))

    async def get_long_poll_settings(self, **params: Any) -> Any:
        return await self._bot(GroupsGetLongPollSettings(**params))

    async def get_members(self, **params: Any) -> Any:
        return await self._bot(GroupsGetMembers(**params))

    async def get_online_status(self, **params: Any) -> Any:
        return await self._bot(GroupsGetOnlineStatus(**params))

    async def get_requests(self, **params: Any) -> Any:
        return await self._bot(GroupsGetRequests(**params))

    async def get_settings(self, **params: Any) -> Any:
        return await self._bot(GroupsGetSettings(**params))

    async def get_tag_list(self, **params: Any) -> Any:
        return await self._bot(GroupsGetTagList(**params))

    async def get_token_permissions(self, **params: Any) -> Any:
        return await self._bot(GroupsGetTokenPermissions(**params))

    async def invite(self, **params: Any) -> Any:
        return await self._bot(GroupsInvite(**params))

    async def is_member(self, **params: Any) -> Any:
        return await self._bot(GroupsIsMember(**params))

    async def join(self, **params: Any) -> Any:
        return await self._bot(GroupsJoin(**params))

    async def leave(self, **params: Any) -> Any:
        return await self._bot(GroupsLeave(**params))

    async def remove_user(self, **params: Any) -> Any:
        return await self._bot(GroupsRemoveUser(**params))

    async def reorder_link(self, **params: Any) -> Any:
        return await self._bot(GroupsReorderLink(**params))

    async def search(self, **params: Any) -> Any:
        return await self._bot(GroupsSearch(**params))

    async def set_callback_settings(self, **params: Any) -> Any:
        return await self._bot(GroupsSetCallbackSettings(**params))

    async def set_long_poll_settings(self, **params: Any) -> Any:
        return await self._bot(GroupsSetLongPollSettings(**params))

    async def set_settings(self, **params: Any) -> Any:
        return await self._bot(GroupsSetSettings(**params))

    async def set_user_note(self, **params: Any) -> Any:
        return await self._bot(GroupsSetUserNote(**params))

    async def tag_add(self, **params: Any) -> Any:
        return await self._bot(GroupsTagAdd(**params))

    async def tag_bind(self, **params: Any) -> Any:
        return await self._bot(GroupsTagBind(**params))

    async def tag_delete(self, **params: Any) -> Any:
        return await self._bot(GroupsTagDelete(**params))

    async def tag_update(self, **params: Any) -> Any:
        return await self._bot(GroupsTagUpdate(**params))

    async def toggle_market(self, **params: Any) -> Any:
        return await self._bot(GroupsToggleMarket(**params))

    async def unban(self, **params: Any) -> Any:
        return await self._bot(GroupsUnban(**params))


class LeadFormsMethods(MethodNamespace):
    async def create(self, **params: Any) -> Any:
        return await self._bot(LeadFormsCreate(**params))

    async def delete(self, **params: Any) -> Any:
        return await self._bot(LeadFormsDelete(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(LeadFormsGet(**params))

    async def get_leads(self, **params: Any) -> Any:
        return await self._bot(LeadFormsGetLeads(**params))

    async def get_upload_u_r_l(self, **params: Any) -> Any:
        return await self._bot(LeadFormsGetUploadURL(**params))

    async def list(self, **params: Any) -> Any:
        return await self._bot(LeadFormsList(**params))

    async def update(self, **params: Any) -> Any:
        return await self._bot(LeadFormsUpdate(**params))


class LikesMethods(MethodNamespace):
    async def add(self, **params: Any) -> Any:
        return await self._bot(LikesAdd(**params))

    async def delete(self, **params: Any) -> Any:
        return await self._bot(LikesDelete(**params))

    async def get_list(self, **params: Any) -> Any:
        return await self._bot(LikesGetList(**params))

    async def is_liked(self, **params: Any) -> Any:
        return await self._bot(LikesIsLiked(**params))


class MarketMethods(MethodNamespace):
    async def add(self, **params: Any) -> Any:
        return await self._bot(MarketAdd(**params))

    async def add_album(self, **params: Any) -> Any:
        return await self._bot(MarketAddAlbum(**params))

    async def add_property(self, **params: Any) -> Any:
        return await self._bot(MarketAddProperty(**params))

    async def add_property_variant(self, **params: Any) -> Any:
        return await self._bot(MarketAddPropertyVariant(**params))

    async def add_to_album(self, **params: Any) -> Any:
        return await self._bot(MarketAddToAlbum(**params))

    async def create_comment(self, **params: Any) -> Any:
        return await self._bot(MarketCreateComment(**params))

    async def delete(self, **params: Any) -> Any:
        return await self._bot(MarketDelete(**params))

    async def delete_album(self, **params: Any) -> Any:
        return await self._bot(MarketDeleteAlbum(**params))

    async def delete_comment(self, **params: Any) -> Any:
        return await self._bot(MarketDeleteComment(**params))

    async def delete_property(self, **params: Any) -> Any:
        return await self._bot(MarketDeleteProperty(**params))

    async def delete_property_variant(self, **params: Any) -> Any:
        return await self._bot(MarketDeletePropertyVariant(**params))

    async def edit(self, **params: Any) -> Any:
        return await self._bot(MarketEdit(**params))

    async def edit_album(self, **params: Any) -> Any:
        return await self._bot(MarketEditAlbum(**params))

    async def edit_comment(self, **params: Any) -> Any:
        return await self._bot(MarketEditComment(**params))

    async def edit_order(self, **params: Any) -> Any:
        return await self._bot(MarketEditOrder(**params))

    async def edit_property(self, **params: Any) -> Any:
        return await self._bot(MarketEditProperty(**params))

    async def edit_property_variant(self, **params: Any) -> Any:
        return await self._bot(MarketEditPropertyVariant(**params))

    async def filter_categories(self, **params: Any) -> Any:
        return await self._bot(MarketFilterCategories(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(MarketGet(**params))

    async def get_album_by_id(self, **params: Any) -> Any:
        return await self._bot(MarketGetAlbumById(**params))

    async def get_albums(self, **params: Any) -> Any:
        return await self._bot(MarketGetAlbums(**params))

    async def get_by_id(self, **params: Any) -> Any:
        return await self._bot(MarketGetById(**params))

    async def get_categories(self, **params: Any) -> Any:
        return await self._bot(MarketGetCategories(**params))

    async def get_comments(self, **params: Any) -> Any:
        return await self._bot(MarketGetComments(**params))

    async def get_faves_for_attach(self, **params: Any) -> Any:
        return await self._bot(MarketGetFavesForAttach(**params))

    async def get_group_orders(self, **params: Any) -> Any:
        return await self._bot(MarketGetGroupOrders(**params))

    async def get_order_by_id(self, **params: Any) -> Any:
        return await self._bot(MarketGetOrderById(**params))

    async def get_order_items(self, **params: Any) -> Any:
        return await self._bot(MarketGetOrderItems(**params))

    async def get_orders(self, **params: Any) -> Any:
        return await self._bot(MarketGetOrders(**params))

    async def get_product_photo_upload_server(self, **params: Any) -> Any:
        return await self._bot(MarketGetProductPhotoUploadServer(**params))

    async def get_properties(self, **params: Any) -> Any:
        return await self._bot(MarketGetProperties(**params))

    async def group_items(self, **params: Any) -> Any:
        return await self._bot(MarketGroupItems(**params))

    async def remove_from_album(self, **params: Any) -> Any:
        return await self._bot(MarketRemoveFromAlbum(**params))

    async def reorder_albums(self, **params: Any) -> Any:
        return await self._bot(MarketReorderAlbums(**params))

    async def reorder_items(self, **params: Any) -> Any:
        return await self._bot(MarketReorderItems(**params))

    async def report(self, **params: Any) -> Any:
        return await self._bot(MarketReport(**params))

    async def report_comment(self, **params: Any) -> Any:
        return await self._bot(MarketReportComment(**params))

    async def restore(self, **params: Any) -> Any:
        return await self._bot(MarketRestore(**params))

    async def restore_comment(self, **params: Any) -> Any:
        return await self._bot(MarketRestoreComment(**params))

    async def save_product_photo(self, **params: Any) -> Any:
        return await self._bot(MarketSaveProductPhoto(**params))

    async def save_product_photo_bulk(self, **params: Any) -> Any:
        return await self._bot(MarketSaveProductPhotoBulk(**params))

    async def search(self, **params: Any) -> Any:
        return await self._bot(MarketSearch(**params))

    async def search_items(self, **params: Any) -> Any:
        return await self._bot(MarketSearchItems(**params))

    async def search_items_basic(self, **params: Any) -> Any:
        return await self._bot(MarketSearchItemsBasic(**params))

    async def ungroup_items(self, **params: Any) -> Any:
        return await self._bot(MarketUngroupItems(**params))


class MessagesMethods(MethodNamespace):
    async def add_chat_user(self, **params: Any) -> Any:
        return await self._bot(MessagesAddChatUser(**params))

    async def add_chat_users(self, **params: Any) -> Any:
        return await self._bot(MessagesAddChatUsers(**params))

    async def allow_messages_from_group(self, **params: Any) -> Any:
        return await self._bot(MessagesAllowMessagesFromGroup(**params))

    async def create_chat(self, **params: Any) -> Any:
        return await self._bot(MessagesCreateChat(**params))

    async def delete(self, **params: Any) -> Any:
        return await self._bot(MessagesDelete(**params))

    async def delete_chat_photo(self, **params: Any) -> Any:
        return await self._bot(MessagesDeleteChatPhoto(**params))

    async def delete_conversation(self, **params: Any) -> Any:
        return await self._bot(MessagesDeleteConversation(**params))

    async def delete_reaction(self, **params: Any) -> Any:
        return await self._bot(MessagesDeleteReaction(**params))

    async def deny_messages_from_group(self, **params: Any) -> Any:
        return await self._bot(MessagesDenyMessagesFromGroup(**params))

    async def edit(self, **params: Any) -> Any:
        return await self._bot(MessagesEdit(**params))

    async def edit_chat(self, **params: Any) -> Any:
        return await self._bot(MessagesEditChat(**params))

    async def get_by_conversation_message_id(self, **params: Any) -> Any:
        return await self._bot(MessagesGetByConversationMessageId(**params))

    async def get_by_id(self, **params: Any) -> Any:
        return await self._bot(MessagesGetById(**params))

    async def get_chat(self, **params: Any) -> Any:
        return await self._bot(MessagesGetChat(**params))

    async def get_chat_preview(self, **params: Any) -> Any:
        return await self._bot(MessagesGetChatPreview(**params))

    async def get_conversation_members(self, **params: Any) -> Any:
        return await self._bot(MessagesGetConversationMembers(**params))

    async def get_conversations(self, **params: Any) -> Any:
        return await self._bot(MessagesGetConversations(**params))

    async def get_conversations_by_id(self, **params: Any) -> Any:
        return await self._bot(MessagesGetConversationsById(**params))

    async def get_history(self, **params: Any) -> Any:
        return await self._bot(MessagesGetHistory(**params))

    async def get_history_attachments(self, **params: Any) -> Any:
        return await self._bot(MessagesGetHistoryAttachments(**params))

    async def get_important_messages(self, **params: Any) -> Any:
        return await self._bot(MessagesGetImportantMessages(**params))

    async def get_intent_users(self, **params: Any) -> Any:
        return await self._bot(MessagesGetIntentUsers(**params))

    async def get_invite_link(self, **params: Any) -> Any:
        return await self._bot(MessagesGetInviteLink(**params))

    async def get_last_activity(self, **params: Any) -> Any:
        return await self._bot(MessagesGetLastActivity(**params))

    async def get_long_poll_history(self, **params: Any) -> Any:
        return await self._bot(MessagesGetLongPollHistory(**params))

    async def get_long_poll_server(self, **params: Any) -> Any:
        return await self._bot(MessagesGetLongPollServer(**params))

    async def get_messages_reactions(self, **params: Any) -> Any:
        return await self._bot(MessagesGetMessagesReactions(**params))

    async def get_reacted_peers(self, **params: Any) -> Any:
        return await self._bot(MessagesGetReactedPeers(**params))

    async def get_reactions_assets(self, **params: Any) -> Any:
        return await self._bot(MessagesGetReactionsAssets(**params))

    async def is_messages_from_group_allowed(self, **params: Any) -> Any:
        return await self._bot(MessagesIsMessagesFromGroupAllowed(**params))

    async def join_chat_by_invite_link(self, **params: Any) -> Any:
        return await self._bot(MessagesJoinChatByInviteLink(**params))

    async def mark_as_answered_conversation(self, **params: Any) -> Any:
        return await self._bot(MessagesMarkAsAnsweredConversation(**params))

    async def mark_as_important(self, **params: Any) -> Any:
        return await self._bot(MessagesMarkAsImportant(**params))

    async def mark_as_important_conversation(self, **params: Any) -> Any:
        return await self._bot(MessagesMarkAsImportantConversation(**params))

    async def mark_as_read(self, **params: Any) -> Any:
        return await self._bot(MessagesMarkAsRead(**params))

    async def mark_reactions_as_read(self, **params: Any) -> Any:
        return await self._bot(MessagesMarkReactionsAsRead(**params))

    async def mute_chat_mentions(self, **params: Any) -> Any:
        return await self._bot(MessagesMuteChatMentions(**params))

    async def pin(self, **params: Any) -> Any:
        return await self._bot(MessagesPin(**params))

    async def remove_chat_user(self, **params: Any) -> Any:
        return await self._bot(MessagesRemoveChatUser(**params))

    async def restore(self, **params: Any) -> Any:
        return await self._bot(MessagesRestore(**params))

    async def search(self, **params: Any) -> Any:
        return await self._bot(MessagesSearch(**params))

    async def search_conversations(self, **params: Any) -> Any:
        return await self._bot(MessagesSearchConversations(**params))

    async def send(self, **params: Any) -> Any:
        return await self._bot(MessagesSend(**params))

    async def send_message_event_answer(self, **params: Any) -> Any:
        return await self._bot(MessagesSendMessageEventAnswer(**params))

    async def send_reaction(self, **params: Any) -> Any:
        return await self._bot(MessagesSendReaction(**params))

    async def set_activity(self, **params: Any) -> Any:
        return await self._bot(MessagesSetActivity(**params))

    async def set_chat_photo(self, **params: Any) -> Any:
        return await self._bot(MessagesSetChatPhoto(**params))

    async def unpin(self, **params: Any) -> Any:
        return await self._bot(MessagesUnpin(**params))


class NewsfeedMethods(MethodNamespace):
    async def add_ban(self, **params: Any) -> Any:
        return await self._bot(NewsfeedAddBan(**params))

    async def delete_ban(self, **params: Any) -> Any:
        return await self._bot(NewsfeedDeleteBan(**params))

    async def delete_list(self, **params: Any) -> Any:
        return await self._bot(NewsfeedDeleteList(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(NewsfeedGet(**params))

    async def get_banned(self, **params: Any) -> Any:
        return await self._bot(NewsfeedGetBanned(**params))

    async def get_comments(self, **params: Any) -> Any:
        return await self._bot(NewsfeedGetComments(**params))

    async def get_lists(self, **params: Any) -> Any:
        return await self._bot(NewsfeedGetLists(**params))

    async def get_mentions(self, **params: Any) -> Any:
        return await self._bot(NewsfeedGetMentions(**params))

    async def get_recommended(self, **params: Any) -> Any:
        return await self._bot(NewsfeedGetRecommended(**params))

    async def get_suggested_sources(self, **params: Any) -> Any:
        return await self._bot(NewsfeedGetSuggestedSources(**params))

    async def ignore_item(self, **params: Any) -> Any:
        return await self._bot(NewsfeedIgnoreItem(**params))

    async def save_list(self, **params: Any) -> Any:
        return await self._bot(NewsfeedSaveList(**params))

    async def search(self, **params: Any) -> Any:
        return await self._bot(NewsfeedSearch(**params))

    async def unignore_item(self, **params: Any) -> Any:
        return await self._bot(NewsfeedUnignoreItem(**params))

    async def unsubscribe(self, **params: Any) -> Any:
        return await self._bot(NewsfeedUnsubscribe(**params))


class NotesMethods(MethodNamespace):
    async def add(self, **params: Any) -> Any:
        return await self._bot(NotesAdd(**params))

    async def create_comment(self, **params: Any) -> Any:
        return await self._bot(NotesCreateComment(**params))

    async def delete(self, **params: Any) -> Any:
        return await self._bot(NotesDelete(**params))

    async def delete_comment(self, **params: Any) -> Any:
        return await self._bot(NotesDeleteComment(**params))

    async def edit(self, **params: Any) -> Any:
        return await self._bot(NotesEdit(**params))

    async def edit_comment(self, **params: Any) -> Any:
        return await self._bot(NotesEditComment(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(NotesGet(**params))

    async def get_by_id(self, **params: Any) -> Any:
        return await self._bot(NotesGetById(**params))

    async def get_comments(self, **params: Any) -> Any:
        return await self._bot(NotesGetComments(**params))

    async def restore_comment(self, **params: Any) -> Any:
        return await self._bot(NotesRestoreComment(**params))


class NotificationsMethods(MethodNamespace):
    async def get(self, **params: Any) -> Any:
        return await self._bot(NotificationsGet(**params))

    async def mark_as_viewed(self, **params: Any) -> Any:
        return await self._bot(NotificationsMarkAsViewed(**params))

    async def send_message(self, **params: Any) -> Any:
        return await self._bot(NotificationsSendMessage(**params))


class OrdersMethods(MethodNamespace):
    async def cancel_subscription(self, **params: Any) -> Any:
        return await self._bot(OrdersCancelSubscription(**params))

    async def change_state(self, **params: Any) -> Any:
        return await self._bot(OrdersChangeState(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(OrdersGet(**params))

    async def get_amount(self, **params: Any) -> Any:
        return await self._bot(OrdersGetAmount(**params))

    async def get_by_id(self, **params: Any) -> Any:
        return await self._bot(OrdersGetById(**params))

    async def get_user_subscription_by_id(self, **params: Any) -> Any:
        return await self._bot(OrdersGetUserSubscriptionById(**params))

    async def get_user_subscriptions(self, **params: Any) -> Any:
        return await self._bot(OrdersGetUserSubscriptions(**params))


class PagesMethods(MethodNamespace):
    async def clear_cache(self, **params: Any) -> Any:
        return await self._bot(PagesClearCache(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(PagesGet(**params))

    async def get_history(self, **params: Any) -> Any:
        return await self._bot(PagesGetHistory(**params))

    async def get_titles(self, **params: Any) -> Any:
        return await self._bot(PagesGetTitles(**params))

    async def get_version(self, **params: Any) -> Any:
        return await self._bot(PagesGetVersion(**params))

    async def parse_wiki(self, **params: Any) -> Any:
        return await self._bot(PagesParseWiki(**params))

    async def save(self, **params: Any) -> Any:
        return await self._bot(PagesSave(**params))

    async def save_access(self, **params: Any) -> Any:
        return await self._bot(PagesSaveAccess(**params))


class PhotosMethods(MethodNamespace):
    async def confirm_tag(self, **params: Any) -> Any:
        return await self._bot(PhotosConfirmTag(**params))

    async def copy(self, **params: Any) -> Any:
        return await self._bot(PhotosCopy(**params))

    async def create_album(self, **params: Any) -> Any:
        return await self._bot(PhotosCreateAlbum(**params))

    async def create_comment(self, **params: Any) -> Any:
        return await self._bot(PhotosCreateComment(**params))

    async def delete(self, **params: Any) -> Any:
        return await self._bot(PhotosDelete(**params))

    async def delete_album(self, **params: Any) -> Any:
        return await self._bot(PhotosDeleteAlbum(**params))

    async def delete_comment(self, **params: Any) -> Any:
        return await self._bot(PhotosDeleteComment(**params))

    async def edit(self, **params: Any) -> Any:
        return await self._bot(PhotosEdit(**params))

    async def edit_album(self, **params: Any) -> Any:
        return await self._bot(PhotosEditAlbum(**params))

    async def edit_comment(self, **params: Any) -> Any:
        return await self._bot(PhotosEditComment(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(PhotosGet(**params))

    async def get_albums(self, **params: Any) -> Any:
        return await self._bot(PhotosGetAlbums(**params))

    async def get_albums_count(self, **params: Any) -> Any:
        return await self._bot(PhotosGetAlbumsCount(**params))

    async def get_all(self, **params: Any) -> Any:
        return await self._bot(PhotosGetAll(**params))

    async def get_all_comments(self, **params: Any) -> Any:
        return await self._bot(PhotosGetAllComments(**params))

    async def get_by_id(self, **params: Any) -> Any:
        return await self._bot(PhotosGetById(**params))

    async def get_chat_upload_server(self, **params: Any) -> Any:
        return await self._bot(PhotosGetChatUploadServer(**params))

    async def get_comments(self, **params: Any) -> Any:
        return await self._bot(PhotosGetComments(**params))

    async def get_market_album_upload_server(self, **params: Any) -> Any:
        return await self._bot(PhotosGetMarketAlbumUploadServer(**params))

    async def get_messages_upload_server(self, **params: Any) -> Any:
        return await self._bot(PhotosGetMessagesUploadServer(**params))

    async def get_new_tags(self, **params: Any) -> Any:
        return await self._bot(PhotosGetNewTags(**params))

    async def get_owner_cover_photo_upload_server(self, **params: Any) -> Any:
        return await self._bot(PhotosGetOwnerCoverPhotoUploadServer(**params))

    async def get_owner_photo_upload_server(self, **params: Any) -> Any:
        return await self._bot(PhotosGetOwnerPhotoUploadServer(**params))

    async def get_tags(self, **params: Any) -> Any:
        return await self._bot(PhotosGetTags(**params))

    async def get_upload_server(self, **params: Any) -> Any:
        return await self._bot(PhotosGetUploadServer(**params))

    async def get_user_photos(self, **params: Any) -> Any:
        return await self._bot(PhotosGetUserPhotos(**params))

    async def get_wall_upload_server(self, **params: Any) -> Any:
        return await self._bot(PhotosGetWallUploadServer(**params))

    async def make_cover(self, **params: Any) -> Any:
        return await self._bot(PhotosMakeCover(**params))

    async def move(self, **params: Any) -> Any:
        return await self._bot(PhotosMove(**params))

    async def put_tag(self, **params: Any) -> Any:
        return await self._bot(PhotosPutTag(**params))

    async def remove_tag(self, **params: Any) -> Any:
        return await self._bot(PhotosRemoveTag(**params))

    async def reorder_albums(self, **params: Any) -> Any:
        return await self._bot(PhotosReorderAlbums(**params))

    async def reorder_photos(self, **params: Any) -> Any:
        return await self._bot(PhotosReorderPhotos(**params))

    async def report(self, **params: Any) -> Any:
        return await self._bot(PhotosReport(**params))

    async def report_comment(self, **params: Any) -> Any:
        return await self._bot(PhotosReportComment(**params))

    async def restore(self, **params: Any) -> Any:
        return await self._bot(PhotosRestore(**params))

    async def restore_comment(self, **params: Any) -> Any:
        return await self._bot(PhotosRestoreComment(**params))

    async def save(self, **params: Any) -> Any:
        return await self._bot(PhotosSave(**params))

    async def save_market_album_photo(self, **params: Any) -> Any:
        return await self._bot(PhotosSaveMarketAlbumPhoto(**params))

    async def save_messages_photo(self, **params: Any) -> Any:
        return await self._bot(PhotosSaveMessagesPhoto(**params))

    async def save_owner_cover_photo(self, **params: Any) -> Any:
        return await self._bot(PhotosSaveOwnerCoverPhoto(**params))

    async def save_owner_photo(self, **params: Any) -> Any:
        return await self._bot(PhotosSaveOwnerPhoto(**params))

    async def save_wall_photo(self, **params: Any) -> Any:
        return await self._bot(PhotosSaveWallPhoto(**params))

    async def search(self, **params: Any) -> Any:
        return await self._bot(PhotosSearch(**params))


class PodcastsMethods(MethodNamespace):
    async def search_podcast(self, **params: Any) -> Any:
        return await self._bot(PodcastsSearchPodcast(**params))


class PollsMethods(MethodNamespace):
    async def add_vote(self, **params: Any) -> Any:
        return await self._bot(PollsAddVote(**params))

    async def create(self, **params: Any) -> Any:
        return await self._bot(PollsCreate(**params))

    async def delete_vote(self, **params: Any) -> Any:
        return await self._bot(PollsDeleteVote(**params))

    async def edit(self, **params: Any) -> Any:
        return await self._bot(PollsEdit(**params))

    async def get_backgrounds(self, **params: Any) -> Any:
        return await self._bot(PollsGetBackgrounds(**params))

    async def get_by_id(self, **params: Any) -> Any:
        return await self._bot(PollsGetById(**params))

    async def get_photo_upload_server(self, **params: Any) -> Any:
        return await self._bot(PollsGetPhotoUploadServer(**params))

    async def get_voters(self, **params: Any) -> Any:
        return await self._bot(PollsGetVoters(**params))

    async def save_photo(self, **params: Any) -> Any:
        return await self._bot(PollsSavePhoto(**params))


class PrettyCardsMethods(MethodNamespace):
    async def create(self, **params: Any) -> Any:
        return await self._bot(PrettyCardsCreate(**params))

    async def delete(self, **params: Any) -> Any:
        return await self._bot(PrettyCardsDelete(**params))

    async def edit(self, **params: Any) -> Any:
        return await self._bot(PrettyCardsEdit(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(PrettyCardsGet(**params))

    async def get_by_id(self, **params: Any) -> Any:
        return await self._bot(PrettyCardsGetById(**params))

    async def get_upload_u_r_l(self, **params: Any) -> Any:
        return await self._bot(PrettyCardsGetUploadURL(**params))


class SearchMethods(MethodNamespace):
    async def get_hints(self, **params: Any) -> Any:
        return await self._bot(SearchGetHints(**params))


class SecureMethods(MethodNamespace):
    async def add_app_event(self, **params: Any) -> Any:
        return await self._bot(SecureAddAppEvent(**params))

    async def check_token(self, **params: Any) -> Any:
        return await self._bot(SecureCheckToken(**params))

    async def get_app_balance(self, **params: Any) -> Any:
        return await self._bot(SecureGetAppBalance(**params))

    async def get_s_m_s_history(self, **params: Any) -> Any:
        return await self._bot(SecureGetSMSHistory(**params))

    async def get_transactions_history(self, **params: Any) -> Any:
        return await self._bot(SecureGetTransactionsHistory(**params))

    async def get_user_level(self, **params: Any) -> Any:
        return await self._bot(SecureGetUserLevel(**params))

    async def give_event_sticker(self, **params: Any) -> Any:
        return await self._bot(SecureGiveEventSticker(**params))

    async def send_notification(self, **params: Any) -> Any:
        return await self._bot(SecureSendNotification(**params))

    async def send_s_m_s_notification(self, **params: Any) -> Any:
        return await self._bot(SecureSendSMSNotification(**params))

    async def set_counter(self, **params: Any) -> Any:
        return await self._bot(SecureSetCounter(**params))


class StatsMethods(MethodNamespace):
    async def get(self, **params: Any) -> Any:
        return await self._bot(StatsGet(**params))

    async def get_post_reach(self, **params: Any) -> Any:
        return await self._bot(StatsGetPostReach(**params))

    async def track_visitor(self, **params: Any) -> Any:
        return await self._bot(StatsTrackVisitor(**params))


class StatusMethods(MethodNamespace):
    async def get(self, **params: Any) -> Any:
        return await self._bot(StatusGet(**params))

    async def set(self, **params: Any) -> Any:
        return await self._bot(StatusSet(**params))


class StorageMethods(MethodNamespace):
    async def get(self, **params: Any) -> Any:
        return await self._bot(StorageGet(**params))

    async def get_keys(self, **params: Any) -> Any:
        return await self._bot(StorageGetKeys(**params))

    async def set(self, **params: Any) -> Any:
        return await self._bot(StorageSet(**params))


class StoreMethods(MethodNamespace):
    async def add_stickers_to_favorite(self, **params: Any) -> Any:
        return await self._bot(StoreAddStickersToFavorite(**params))

    async def get_favorite_stickers(self, **params: Any) -> Any:
        return await self._bot(StoreGetFavoriteStickers(**params))

    async def get_products(self, **params: Any) -> Any:
        return await self._bot(StoreGetProducts(**params))

    async def get_stickers_keywords(self, **params: Any) -> Any:
        return await self._bot(StoreGetStickersKeywords(**params))

    async def remove_stickers_from_favorite(self, **params: Any) -> Any:
        return await self._bot(StoreRemoveStickersFromFavorite(**params))


class StoriesMethods(MethodNamespace):
    async def ban_owner(self, **params: Any) -> Any:
        return await self._bot(StoriesBanOwner(**params))

    async def delete(self, **params: Any) -> Any:
        return await self._bot(StoriesDelete(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(StoriesGet(**params))

    async def get_banned(self, **params: Any) -> Any:
        return await self._bot(StoriesGetBanned(**params))

    async def get_by_id(self, **params: Any) -> Any:
        return await self._bot(StoriesGetById(**params))

    async def get_photo_upload_server(self, **params: Any) -> Any:
        return await self._bot(StoriesGetPhotoUploadServer(**params))

    async def get_replies(self, **params: Any) -> Any:
        return await self._bot(StoriesGetReplies(**params))

    async def get_stats(self, **params: Any) -> Any:
        return await self._bot(StoriesGetStats(**params))

    async def get_video_upload_server(self, **params: Any) -> Any:
        return await self._bot(StoriesGetVideoUploadServer(**params))

    async def get_viewers(self, **params: Any) -> Any:
        return await self._bot(StoriesGetViewers(**params))

    async def hide_all_replies(self, **params: Any) -> Any:
        return await self._bot(StoriesHideAllReplies(**params))

    async def hide_reply(self, **params: Any) -> Any:
        return await self._bot(StoriesHideReply(**params))

    async def save(self, **params: Any) -> Any:
        return await self._bot(StoriesSave(**params))

    async def search(self, **params: Any) -> Any:
        return await self._bot(StoriesSearch(**params))

    async def send_interaction(self, **params: Any) -> Any:
        return await self._bot(StoriesSendInteraction(**params))

    async def unban_owner(self, **params: Any) -> Any:
        return await self._bot(StoriesUnbanOwner(**params))


class StreamingMethods(MethodNamespace):
    async def get_server_url(self, **params: Any) -> Any:
        return await self._bot(StreamingGetServerUrl(**params))

    async def get_stats(self, **params: Any) -> Any:
        return await self._bot(StreamingGetStats(**params))

    async def get_stem(self, **params: Any) -> Any:
        return await self._bot(StreamingGetStem(**params))


class TranslationsMethods(MethodNamespace):
    async def translate(self, **params: Any) -> Any:
        return await self._bot(TranslationsTranslate(**params))


class UsersMethods(MethodNamespace):
    async def get(self, **params: Any) -> Any:
        return await self._bot(UsersGet(**params))

    async def get_followers(self, **params: Any) -> Any:
        return await self._bot(UsersGetFollowers(**params))

    async def get_subscriptions(self, **params: Any) -> Any:
        return await self._bot(UsersGetSubscriptions(**params))

    async def report(self, **params: Any) -> Any:
        return await self._bot(UsersReport(**params))

    async def search(self, **params: Any) -> Any:
        return await self._bot(UsersSearch(**params))


class UtilsMethods(MethodNamespace):
    async def check_link(self, **params: Any) -> Any:
        return await self._bot(UtilsCheckLink(**params))

    async def delete_from_last_shortened(self, **params: Any) -> Any:
        return await self._bot(UtilsDeleteFromLastShortened(**params))

    async def get_last_shortened_links(self, **params: Any) -> Any:
        return await self._bot(UtilsGetLastShortenedLinks(**params))

    async def get_link_stats(self, **params: Any) -> Any:
        return await self._bot(UtilsGetLinkStats(**params))

    async def get_server_time(self, **params: Any) -> Any:
        return await self._bot(UtilsGetServerTime(**params))

    async def get_short_link(self, **params: Any) -> Any:
        return await self._bot(UtilsGetShortLink(**params))

    async def resolve_screen_name(self, **params: Any) -> Any:
        return await self._bot(UtilsResolveScreenName(**params))


class VideoMethods(MethodNamespace):
    async def add(self, **params: Any) -> Any:
        return await self._bot(VideoAdd(**params))

    async def add_album(self, **params: Any) -> Any:
        return await self._bot(VideoAddAlbum(**params))

    async def add_to_album(self, **params: Any) -> Any:
        return await self._bot(VideoAddToAlbum(**params))

    async def create_comment(self, **params: Any) -> Any:
        return await self._bot(VideoCreateComment(**params))

    async def delete(self, **params: Any) -> Any:
        return await self._bot(VideoDelete(**params))

    async def delete_album(self, **params: Any) -> Any:
        return await self._bot(VideoDeleteAlbum(**params))

    async def delete_comment(self, **params: Any) -> Any:
        return await self._bot(VideoDeleteComment(**params))

    async def delete_thread(self, **params: Any) -> Any:
        return await self._bot(VideoDeleteThread(**params))

    async def edit(self, **params: Any) -> Any:
        return await self._bot(VideoEdit(**params))

    async def edit_album(self, **params: Any) -> Any:
        return await self._bot(VideoEditAlbum(**params))

    async def edit_comment(self, **params: Any) -> Any:
        return await self._bot(VideoEditComment(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(VideoGet(**params))

    async def get_album_by_id(self, **params: Any) -> Any:
        return await self._bot(VideoGetAlbumById(**params))

    async def get_albums(self, **params: Any) -> Any:
        return await self._bot(VideoGetAlbums(**params))

    async def get_albums_by_video(self, **params: Any) -> Any:
        return await self._bot(VideoGetAlbumsByVideo(**params))

    async def get_comments(self, **params: Any) -> Any:
        return await self._bot(VideoGetComments(**params))

    async def get_long_poll_server(self, **params: Any) -> Any:
        return await self._bot(VideoGetLongPollServer(**params))

    async def get_oembed(self, **params: Any) -> Any:
        return await self._bot(VideoGetOembed(**params))

    async def get_thumb_upload_url(self, **params: Any) -> Any:
        return await self._bot(VideoGetThumbUploadUrl(**params))

    async def live_get_categories(self, **params: Any) -> Any:
        return await self._bot(VideoLiveGetCategories(**params))

    async def remove_from_album(self, **params: Any) -> Any:
        return await self._bot(VideoRemoveFromAlbum(**params))

    async def reorder_albums(self, **params: Any) -> Any:
        return await self._bot(VideoReorderAlbums(**params))

    async def reorder_videos(self, **params: Any) -> Any:
        return await self._bot(VideoReorderVideos(**params))

    async def report(self, **params: Any) -> Any:
        return await self._bot(VideoReport(**params))

    async def report_comment(self, **params: Any) -> Any:
        return await self._bot(VideoReportComment(**params))

    async def restore(self, **params: Any) -> Any:
        return await self._bot(VideoRestore(**params))

    async def restore_comment(self, **params: Any) -> Any:
        return await self._bot(VideoRestoreComment(**params))

    async def restore_thread(self, **params: Any) -> Any:
        return await self._bot(VideoRestoreThread(**params))

    async def save(self, **params: Any) -> Any:
        return await self._bot(VideoSave(**params))

    async def save_uploaded_thumb(self, **params: Any) -> Any:
        return await self._bot(VideoSaveUploadedThumb(**params))

    async def search(self, **params: Any) -> Any:
        return await self._bot(VideoSearch(**params))

    async def start_streaming(self, **params: Any) -> Any:
        return await self._bot(VideoStartStreaming(**params))

    async def stop_streaming(self, **params: Any) -> Any:
        return await self._bot(VideoStopStreaming(**params))

    async def unpin_comment(self, **params: Any) -> Any:
        return await self._bot(VideoUnpinComment(**params))


class WallMethods(MethodNamespace):
    async def check_copyright_link(self, **params: Any) -> Any:
        return await self._bot(WallCheckCopyrightLink(**params))

    async def close_comments(self, **params: Any) -> Any:
        return await self._bot(WallCloseComments(**params))

    async def create_comment(self, **params: Any) -> Any:
        return await self._bot(WallCreateComment(**params))

    async def delete(self, **params: Any) -> Any:
        return await self._bot(WallDelete(**params))

    async def delete_comment(self, **params: Any) -> Any:
        return await self._bot(WallDeleteComment(**params))

    async def edit(self, **params: Any) -> Any:
        return await self._bot(WallEdit(**params))

    async def edit_ads_stealth(self, **params: Any) -> Any:
        return await self._bot(WallEditAdsStealth(**params))

    async def edit_comment(self, **params: Any) -> Any:
        return await self._bot(WallEditComment(**params))

    async def get(self, **params: Any) -> Any:
        return await self._bot(WallGet(**params))

    async def get_by_id(self, **params: Any) -> Any:
        return await self._bot(WallGetById(**params))

    async def get_comment(self, **params: Any) -> Any:
        return await self._bot(WallGetComment(**params))

    async def get_comments(self, **params: Any) -> Any:
        return await self._bot(WallGetComments(**params))

    async def get_reposts(self, **params: Any) -> Any:
        return await self._bot(WallGetReposts(**params))

    async def open_comments(self, **params: Any) -> Any:
        return await self._bot(WallOpenComments(**params))

    async def parse_attached_link(self, **params: Any) -> Any:
        return await self._bot(WallParseAttachedLink(**params))

    async def pin(self, **params: Any) -> Any:
        return await self._bot(WallPin(**params))

    async def post(self, **params: Any) -> Any:
        return await self._bot(WallPost(**params))

    async def post_ads_stealth(self, **params: Any) -> Any:
        return await self._bot(WallPostAdsStealth(**params))

    async def report_comment(self, **params: Any) -> Any:
        return await self._bot(WallReportComment(**params))

    async def report_post(self, **params: Any) -> Any:
        return await self._bot(WallReportPost(**params))

    async def repost(self, **params: Any) -> Any:
        return await self._bot(WallRepost(**params))

    async def restore(self, **params: Any) -> Any:
        return await self._bot(WallRestore(**params))

    async def restore_comment(self, **params: Any) -> Any:
        return await self._bot(WallRestoreComment(**params))

    async def search(self, **params: Any) -> Any:
        return await self._bot(WallSearch(**params))

    async def unpin(self, **params: Any) -> Any:
        return await self._bot(WallUnpin(**params))


class WidgetsMethods(MethodNamespace):
    async def get_comments(self, **params: Any) -> Any:
        return await self._bot(WidgetsGetComments(**params))

    async def get_pages(self, **params: Any) -> Any:
        return await self._bot(WidgetsGetPages(**params))


METHOD_GROUPS: dict[str, type[MethodNamespace]] = {
    'account': AccountMethods,
    'ads': AdsMethods,
    'api': ApiMethods,
    'appWidgets': AppWidgetsMethods,
    'apps': AppsMethods,
    'auth': AuthMethods,
    'board': BoardMethods,
    'bugtracker': BugtrackerMethods,
    'calls': CallsMethods,
    'database': DatabaseMethods,
    'docs': DocsMethods,
    'donut': DonutMethods,
    'downloadedGames': DownloadedGamesMethods,
    'fave': FaveMethods,
    'friends': FriendsMethods,
    'gifts': GiftsMethods,
    'groups': GroupsMethods,
    'leadForms': LeadFormsMethods,
    'likes': LikesMethods,
    'market': MarketMethods,
    'messages': MessagesMethods,
    'newsfeed': NewsfeedMethods,
    'notes': NotesMethods,
    'notifications': NotificationsMethods,
    'orders': OrdersMethods,
    'pages': PagesMethods,
    'photos': PhotosMethods,
    'podcasts': PodcastsMethods,
    'polls': PollsMethods,
    'prettyCards': PrettyCardsMethods,
    'search': SearchMethods,
    'secure': SecureMethods,
    'stats': StatsMethods,
    'status': StatusMethods,
    'storage': StorageMethods,
    'store': StoreMethods,
    'stories': StoriesMethods,
    'streaming': StreamingMethods,
    'translations': TranslationsMethods,
    'users': UsersMethods,
    'utils': UtilsMethods,
    'video': VideoMethods,
    'wall': WallMethods,
    'widgets': WidgetsMethods,
}

__all__ = [
    'METHOD_GROUPS',
    'MethodNamespace',
    'AccountBan',
    'AccountChangePassword',
    'AccountGetActiveOffers',
    'AccountGetAppPermissions',
    'AccountGetBanned',
    'AccountGetCounters',
    'AccountGetInfo',
    'AccountGetProfileInfo',
    'AccountGetPushSettings',
    'AccountRegisterDevice',
    'AccountSaveProfileInfo',
    'AccountSetInfo',
    'AccountSetOffline',
    'AccountSetOnline',
    'AccountSetPushSettings',
    'AccountSetSilenceMode',
    'AccountUnban',
    'AccountUnregisterDevice',
    'AdsAddOfficeUsers',
    'AdsCheckLink',
    'AdsCreateAds',
    'AdsCreateCampaigns',
    'AdsCreateClients',
    'AdsCreateLookalikeRequest',
    'AdsCreateTargetGroup',
    'AdsCreateTargetPixel',
    'AdsDeleteAds',
    'AdsDeleteCampaigns',
    'AdsDeleteClients',
    'AdsDeleteTargetGroup',
    'AdsDeleteTargetPixel',
    'AdsGetAccounts',
    'AdsGetAds',
    'AdsGetAdsLayout',
    'AdsGetAdsTargeting',
    'AdsGetBudget',
    'AdsGetCampaigns',
    'AdsGetCategories',
    'AdsGetClients',
    'AdsGetDemographics',
    'AdsGetFloodStats',
    'AdsGetLookalikeRequests',
    'AdsGetMusicians',
    'AdsGetMusiciansByIds',
    'AdsGetOfficeUsers',
    'AdsGetPostsReach',
    'AdsGetRejectionReason',
    'AdsGetStatistics',
    'AdsGetSuggestions',
    'AdsGetTargetGroups',
    'AdsGetTargetPixels',
    'AdsGetTargetingStats',
    'AdsGetUploadURL',
    'AdsGetVideoUploadURL',
    'AdsImportTargetContacts',
    'AdsRemoveOfficeUsers',
    'AdsRemoveTargetContacts',
    'AdsSaveLookalikeRequestResult',
    'AdsShareTargetGroup',
    'AdsUpdateAds',
    'AdsUpdateCampaigns',
    'AdsUpdateClients',
    'AdsUpdateOfficeUsers',
    'AdsUpdateTargetGroup',
    'AdsUpdateTargetPixel',
    'AppWidgetsGetAppImageUploadServer',
    'AppWidgetsGetAppImages',
    'AppWidgetsGetGroupImageUploadServer',
    'AppWidgetsGetGroupImages',
    'AppWidgetsGetImagesById',
    'AppWidgetsSaveAppImage',
    'AppWidgetsSaveGroupImage',
    'AppWidgetsUpdate',
    'AppsAddSnippet',
    'AppsAddUsersToTestingGroup',
    'AppsDeleteAppRequests',
    'AppsDeleteSnippet',
    'AppsGet',
    'AppsGetCatalog',
    'AppsGetFriendsList',
    'AppsGetLeaderboard',
    'AppsGetMiniAppPolicies',
    'AppsGetScopes',
    'AppsGetScore',
    'AppsGetSnippets',
    'AppsGetTestingGroups',
    'AppsIsNotificationsAllowed',
    'AppsPromoHasActiveGift',
    'AppsPromoUseGift',
    'AppsRemoveTestingGroup',
    'AppsRemoveUsersFromTestingGroups',
    'AppsSendRequest',
    'AppsUpdateMetaForTestingGroup',
    'AuthRestore',
    'BoardAddTopic',
    'BoardCloseTopic',
    'BoardCreateComment',
    'BoardDeleteComment',
    'BoardDeleteTopic',
    'BoardEditComment',
    'BoardEditTopic',
    'BoardFixTopic',
    'BoardGetComments',
    'BoardGetTopics',
    'BoardOpenTopic',
    'BoardRestoreComment',
    'BoardUnfixTopic',
    'BugtrackerAddCompanyGroupsMembers',
    'BugtrackerAddCompanyMembers',
    'BugtrackerChangeBugreportStatus',
    'BugtrackerCreateComment',
    'BugtrackerGetBugreportById',
    'BugtrackerGetCompanyGroupMembers',
    'BugtrackerGetCompanyMembers',
    'BugtrackerGetDownloadVersionUrl',
    'BugtrackerGetProductBuildUploadServer',
    'BugtrackerRemoveCompanyGroupMember',
    'BugtrackerRemoveCompanyMember',
    'BugtrackerSaveProductVersion',
    'BugtrackerSetCompanyMemberRole',
    'BugtrackerSetProductIsOver',
    'CallsForceFinish',
    'CallsStart',
    'DatabaseGetChairs',
    'DatabaseGetCities',
    'DatabaseGetCitiesById',
    'DatabaseGetCountries',
    'DatabaseGetCountriesById',
    'DatabaseGetFaculties',
    'DatabaseGetMetroStations',
    'DatabaseGetMetroStationsById',
    'DatabaseGetRegions',
    'DatabaseGetSchoolClasses',
    'DatabaseGetSchools',
    'DatabaseGetUniversities',
    'DocsAdd',
    'DocsDelete',
    'DocsEdit',
    'DocsGet',
    'DocsGetById',
    'DocsGetMessagesUploadServer',
    'DocsGetTypes',
    'DocsGetUploadServer',
    'DocsGetWallUploadServer',
    'DocsRestore',
    'DocsSave',
    'DocsSearch',
    'DonutGetFriends',
    'DonutGetSubscription',
    'DonutGetSubscriptions',
    'DonutIsDon',
    'DownloadedGamesGetPaidStatus',
    'Execute',
    'FaveAddArticle',
    'FaveAddLink',
    'FaveAddPage',
    'FaveAddPost',
    'FaveAddProduct',
    'FaveAddTag',
    'FaveAddVideo',
    'FaveEditTag',
    'FaveGet',
    'FaveGetPages',
    'FaveGetTags',
    'FaveMarkSeen',
    'FaveRemoveArticle',
    'FaveRemoveLink',
    'FaveRemovePage',
    'FaveRemovePost',
    'FaveRemoveProduct',
    'FaveRemoveTag',
    'FaveRemoveVideo',
    'FaveReorderTags',
    'FaveSetPageTags',
    'FaveSetTags',
    'FaveTrackPageInteraction',
    'FriendsAdd',
    'FriendsAddList',
    'FriendsAreFriends',
    'FriendsDelete',
    'FriendsDeleteAllRequests',
    'FriendsDeleteList',
    'FriendsEdit',
    'FriendsEditList',
    'FriendsGet',
    'FriendsGetAppUsers',
    'FriendsGetLists',
    'FriendsGetMutual',
    'FriendsGetOnline',
    'FriendsGetRecent',
    'FriendsGetRequests',
    'FriendsGetSuggestions',
    'FriendsSearch',
    'GiftsGet',
    'GroupsAddAddress',
    'GroupsAddCallbackServer',
    'GroupsAddLink',
    'GroupsApproveRequest',
    'GroupsBan',
    'GroupsCreate',
    'GroupsDeleteAddress',
    'GroupsDeleteCallbackServer',
    'GroupsDeleteLink',
    'GroupsDisableOnline',
    'GroupsEdit',
    'GroupsEditAddress',
    'GroupsEditCallbackServer',
    'GroupsEditLink',
    'GroupsEditManager',
    'GroupsEnableOnline',
    'GroupsGet',
    'GroupsGetAddresses',
    'GroupsGetBanned',
    'GroupsGetById',
    'GroupsGetCallbackConfirmationCode',
    'GroupsGetCallbackServers',
    'GroupsGetCallbackSettings',
    'GroupsGetCatalogInfo',
    'GroupsGetInvitedUsers',
    'GroupsGetInvites',
    'GroupsGetLongPollServer',
    'GroupsGetLongPollSettings',
    'GroupsGetMembers',
    'GroupsGetOnlineStatus',
    'GroupsGetRequests',
    'GroupsGetSettings',
    'GroupsGetTagList',
    'GroupsGetTokenPermissions',
    'GroupsInvite',
    'GroupsIsMember',
    'GroupsJoin',
    'GroupsLeave',
    'GroupsRemoveUser',
    'GroupsReorderLink',
    'GroupsSearch',
    'GroupsSetCallbackSettings',
    'GroupsSetLongPollSettings',
    'GroupsSetSettings',
    'GroupsSetUserNote',
    'GroupsTagAdd',
    'GroupsTagBind',
    'GroupsTagDelete',
    'GroupsTagUpdate',
    'GroupsToggleMarket',
    'GroupsUnban',
    'LeadFormsCreate',
    'LeadFormsDelete',
    'LeadFormsGet',
    'LeadFormsGetLeads',
    'LeadFormsGetUploadURL',
    'LeadFormsList',
    'LeadFormsUpdate',
    'LikesAdd',
    'LikesDelete',
    'LikesGetList',
    'LikesIsLiked',
    'MarketAdd',
    'MarketAddAlbum',
    'MarketAddProperty',
    'MarketAddPropertyVariant',
    'MarketAddToAlbum',
    'MarketCreateComment',
    'MarketDelete',
    'MarketDeleteAlbum',
    'MarketDeleteComment',
    'MarketDeleteProperty',
    'MarketDeletePropertyVariant',
    'MarketEdit',
    'MarketEditAlbum',
    'MarketEditComment',
    'MarketEditOrder',
    'MarketEditProperty',
    'MarketEditPropertyVariant',
    'MarketFilterCategories',
    'MarketGet',
    'MarketGetAlbumById',
    'MarketGetAlbums',
    'MarketGetById',
    'MarketGetCategories',
    'MarketGetComments',
    'MarketGetFavesForAttach',
    'MarketGetGroupOrders',
    'MarketGetOrderById',
    'MarketGetOrderItems',
    'MarketGetOrders',
    'MarketGetProductPhotoUploadServer',
    'MarketGetProperties',
    'MarketGroupItems',
    'MarketRemoveFromAlbum',
    'MarketReorderAlbums',
    'MarketReorderItems',
    'MarketReport',
    'MarketReportComment',
    'MarketRestore',
    'MarketRestoreComment',
    'MarketSaveProductPhoto',
    'MarketSaveProductPhotoBulk',
    'MarketSearch',
    'MarketSearchItems',
    'MarketSearchItemsBasic',
    'MarketUngroupItems',
    'MessagesAddChatUser',
    'MessagesAddChatUsers',
    'MessagesAllowMessagesFromGroup',
    'MessagesCreateChat',
    'MessagesDelete',
    'MessagesDeleteChatPhoto',
    'MessagesDeleteConversation',
    'MessagesDeleteReaction',
    'MessagesDenyMessagesFromGroup',
    'MessagesEdit',
    'MessagesEditChat',
    'MessagesGetByConversationMessageId',
    'MessagesGetById',
    'MessagesGetChat',
    'MessagesGetChatPreview',
    'MessagesGetConversationMembers',
    'MessagesGetConversations',
    'MessagesGetConversationsById',
    'MessagesGetHistory',
    'MessagesGetHistoryAttachments',
    'MessagesGetImportantMessages',
    'MessagesGetIntentUsers',
    'MessagesGetInviteLink',
    'MessagesGetLastActivity',
    'MessagesGetLongPollHistory',
    'MessagesGetLongPollServer',
    'MessagesGetMessagesReactions',
    'MessagesGetReactedPeers',
    'MessagesGetReactionsAssets',
    'MessagesIsMessagesFromGroupAllowed',
    'MessagesJoinChatByInviteLink',
    'MessagesMarkAsAnsweredConversation',
    'MessagesMarkAsImportant',
    'MessagesMarkAsImportantConversation',
    'MessagesMarkAsRead',
    'MessagesMarkReactionsAsRead',
    'MessagesMuteChatMentions',
    'MessagesPin',
    'MessagesRemoveChatUser',
    'MessagesRestore',
    'MessagesSearch',
    'MessagesSearchConversations',
    'MessagesSend',
    'MessagesSendMessageEventAnswer',
    'MessagesSendReaction',
    'MessagesSetActivity',
    'MessagesSetChatPhoto',
    'MessagesUnpin',
    'NewsfeedAddBan',
    'NewsfeedDeleteBan',
    'NewsfeedDeleteList',
    'NewsfeedGet',
    'NewsfeedGetBanned',
    'NewsfeedGetComments',
    'NewsfeedGetLists',
    'NewsfeedGetMentions',
    'NewsfeedGetRecommended',
    'NewsfeedGetSuggestedSources',
    'NewsfeedIgnoreItem',
    'NewsfeedSaveList',
    'NewsfeedSearch',
    'NewsfeedUnignoreItem',
    'NewsfeedUnsubscribe',
    'NotesAdd',
    'NotesCreateComment',
    'NotesDelete',
    'NotesDeleteComment',
    'NotesEdit',
    'NotesEditComment',
    'NotesGet',
    'NotesGetById',
    'NotesGetComments',
    'NotesRestoreComment',
    'NotificationsGet',
    'NotificationsMarkAsViewed',
    'NotificationsSendMessage',
    'OrdersCancelSubscription',
    'OrdersChangeState',
    'OrdersGet',
    'OrdersGetAmount',
    'OrdersGetById',
    'OrdersGetUserSubscriptionById',
    'OrdersGetUserSubscriptions',
    'PagesClearCache',
    'PagesGet',
    'PagesGetHistory',
    'PagesGetTitles',
    'PagesGetVersion',
    'PagesParseWiki',
    'PagesSave',
    'PagesSaveAccess',
    'PhotosConfirmTag',
    'PhotosCopy',
    'PhotosCreateAlbum',
    'PhotosCreateComment',
    'PhotosDelete',
    'PhotosDeleteAlbum',
    'PhotosDeleteComment',
    'PhotosEdit',
    'PhotosEditAlbum',
    'PhotosEditComment',
    'PhotosGet',
    'PhotosGetAlbums',
    'PhotosGetAlbumsCount',
    'PhotosGetAll',
    'PhotosGetAllComments',
    'PhotosGetById',
    'PhotosGetChatUploadServer',
    'PhotosGetComments',
    'PhotosGetMarketAlbumUploadServer',
    'PhotosGetMessagesUploadServer',
    'PhotosGetNewTags',
    'PhotosGetOwnerCoverPhotoUploadServer',
    'PhotosGetOwnerPhotoUploadServer',
    'PhotosGetTags',
    'PhotosGetUploadServer',
    'PhotosGetUserPhotos',
    'PhotosGetWallUploadServer',
    'PhotosMakeCover',
    'PhotosMove',
    'PhotosPutTag',
    'PhotosRemoveTag',
    'PhotosReorderAlbums',
    'PhotosReorderPhotos',
    'PhotosReport',
    'PhotosReportComment',
    'PhotosRestore',
    'PhotosRestoreComment',
    'PhotosSave',
    'PhotosSaveMarketAlbumPhoto',
    'PhotosSaveMessagesPhoto',
    'PhotosSaveOwnerCoverPhoto',
    'PhotosSaveOwnerPhoto',
    'PhotosSaveWallPhoto',
    'PhotosSearch',
    'PodcastsSearchPodcast',
    'PollsAddVote',
    'PollsCreate',
    'PollsDeleteVote',
    'PollsEdit',
    'PollsGetBackgrounds',
    'PollsGetById',
    'PollsGetPhotoUploadServer',
    'PollsGetVoters',
    'PollsSavePhoto',
    'PrettyCardsCreate',
    'PrettyCardsDelete',
    'PrettyCardsEdit',
    'PrettyCardsGet',
    'PrettyCardsGetById',
    'PrettyCardsGetUploadURL',
    'SearchGetHints',
    'SecureAddAppEvent',
    'SecureCheckToken',
    'SecureGetAppBalance',
    'SecureGetSMSHistory',
    'SecureGetTransactionsHistory',
    'SecureGetUserLevel',
    'SecureGiveEventSticker',
    'SecureSendNotification',
    'SecureSendSMSNotification',
    'SecureSetCounter',
    'StatsGet',
    'StatsGetPostReach',
    'StatsTrackVisitor',
    'StatusGet',
    'StatusSet',
    'StorageGet',
    'StorageGetKeys',
    'StorageSet',
    'StoreAddStickersToFavorite',
    'StoreGetFavoriteStickers',
    'StoreGetProducts',
    'StoreGetStickersKeywords',
    'StoreRemoveStickersFromFavorite',
    'StoriesBanOwner',
    'StoriesDelete',
    'StoriesGet',
    'StoriesGetBanned',
    'StoriesGetById',
    'StoriesGetPhotoUploadServer',
    'StoriesGetReplies',
    'StoriesGetStats',
    'StoriesGetVideoUploadServer',
    'StoriesGetViewers',
    'StoriesHideAllReplies',
    'StoriesHideReply',
    'StoriesSave',
    'StoriesSearch',
    'StoriesSendInteraction',
    'StoriesUnbanOwner',
    'StreamingGetServerUrl',
    'StreamingGetStats',
    'StreamingGetStem',
    'TranslationsTranslate',
    'UsersGet',
    'UsersGetFollowers',
    'UsersGetSubscriptions',
    'UsersReport',
    'UsersSearch',
    'UtilsCheckLink',
    'UtilsDeleteFromLastShortened',
    'UtilsGetLastShortenedLinks',
    'UtilsGetLinkStats',
    'UtilsGetServerTime',
    'UtilsGetShortLink',
    'UtilsResolveScreenName',
    'VideoAdd',
    'VideoAddAlbum',
    'VideoAddToAlbum',
    'VideoCreateComment',
    'VideoDelete',
    'VideoDeleteAlbum',
    'VideoDeleteComment',
    'VideoDeleteThread',
    'VideoEdit',
    'VideoEditAlbum',
    'VideoEditComment',
    'VideoGet',
    'VideoGetAlbumById',
    'VideoGetAlbums',
    'VideoGetAlbumsByVideo',
    'VideoGetComments',
    'VideoGetLongPollServer',
    'VideoGetOembed',
    'VideoGetThumbUploadUrl',
    'VideoLiveGetCategories',
    'VideoRemoveFromAlbum',
    'VideoReorderAlbums',
    'VideoReorderVideos',
    'VideoReport',
    'VideoReportComment',
    'VideoRestore',
    'VideoRestoreComment',
    'VideoRestoreThread',
    'VideoSave',
    'VideoSaveUploadedThumb',
    'VideoSearch',
    'VideoStartStreaming',
    'VideoStopStreaming',
    'VideoUnpinComment',
    'WallCheckCopyrightLink',
    'WallCloseComments',
    'WallCreateComment',
    'WallDelete',
    'WallDeleteComment',
    'WallEdit',
    'WallEditAdsStealth',
    'WallEditComment',
    'WallGet',
    'WallGetById',
    'WallGetComment',
    'WallGetComments',
    'WallGetReposts',
    'WallOpenComments',
    'WallParseAttachedLink',
    'WallPin',
    'WallPost',
    'WallPostAdsStealth',
    'WallReportComment',
    'WallReportPost',
    'WallRepost',
    'WallRestore',
    'WallRestoreComment',
    'WallSearch',
    'WallUnpin',
    'WidgetsGetComments',
    'WidgetsGetPages',
    'AccountMethods',
    'AdsMethods',
    'ApiMethods',
    'AppWidgetsMethods',
    'AppsMethods',
    'AuthMethods',
    'BoardMethods',
    'BugtrackerMethods',
    'CallsMethods',
    'DatabaseMethods',
    'DocsMethods',
    'DonutMethods',
    'DownloadedGamesMethods',
    'FaveMethods',
    'FriendsMethods',
    'GiftsMethods',
    'GroupsMethods',
    'LeadFormsMethods',
    'LikesMethods',
    'MarketMethods',
    'MessagesMethods',
    'NewsfeedMethods',
    'NotesMethods',
    'NotificationsMethods',
    'OrdersMethods',
    'PagesMethods',
    'PhotosMethods',
    'PodcastsMethods',
    'PollsMethods',
    'PrettyCardsMethods',
    'SearchMethods',
    'SecureMethods',
    'StatsMethods',
    'StatusMethods',
    'StorageMethods',
    'StoreMethods',
    'StoriesMethods',
    'StreamingMethods',
    'TranslationsMethods',
    'UsersMethods',
    'UtilsMethods',
    'VideoMethods',
    'WallMethods',
    'WidgetsMethods',
]
