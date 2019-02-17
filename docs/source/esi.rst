ESI API
#######

.. toctree::
   :maxdepth: 4
   :caption: Namespaces

.. autosummary::
   :toctree: generated
   
Alliance
--------

.. py:class:: Alliance

   .. py:method:: get_alliances()

   List all alliances

      :return: List of Alliance IDs
      :rtype: list


   .. py:method:: get_alliances_alliance_id(alliance_id=None)

   Get alliance information

      :param int alliance_id: An EVE alliance ID
      :return: Public data about an alliance
      :rtype: dict


   .. py:method:: get_alliances_alliance_id_corporations(alliance_id=None)

   List alliance's corporations

      :param int alliance_id: An EVE alliance ID
      :return: List of corporation IDs
      :rtype: list


   .. py:method:: get_alliances_alliance_id_icons(alliance_id=None)

   Get alliance icon

      :param int alliance_id: An EVE alliance ID
      :return: Icon URLs for the given alliance id and server
      :rtype: dict




Assets
------

.. py:class:: Assets

   .. py:method:: get_characters_character_id_assets(character_id=None, _token=None)

   Get character assets

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A flat list of the users assets
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_assets(corporation_id=None, _token=None)

   Get corporation assets

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of assets
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: post_characters_character_id_assets_locations(character_id=None, item_ids=None, _token=None)

   Get character asset locations

      :param int character_id: An EVE character ID
      :param None item_ids: A list of item ids
      :param str _token: ESI authorization token
      :return: List of asset locations
      :rtype: list


   .. py:method:: post_characters_character_id_assets_names(character_id=None, item_ids=None, _token=None)

   Get character asset names

      :param int character_id: An EVE character ID
      :param None item_ids: A list of item ids
      :param str _token: ESI authorization token
      :return: List of asset names
      :rtype: list


   .. py:method:: post_corporations_corporation_id_assets_locations(corporation_id=None, item_ids=None, _token=None)

   Get corporation asset locations

      :param int corporation_id: An EVE corporation ID
      :param None item_ids: A list of item ids
      :param str _token: ESI authorization token
      :return: List of asset locations
      :rtype: list


   .. py:method:: post_corporations_corporation_id_assets_names(corporation_id=None, item_ids=None, _token=None)

   Get corporation asset names

      :param int corporation_id: An EVE corporation ID
      :param None item_ids: A list of item ids
      :param str _token: ESI authorization token
      :return: List of asset names
      :rtype: list




Bookmarks
---------

.. py:class:: Bookmarks

   .. py:method:: get_characters_character_id_bookmarks(character_id=None, _token=None)

   List bookmarks

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of bookmarks
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_characters_character_id_bookmarks_folders(character_id=None, _token=None)

   List bookmark folders

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: List of bookmark folders
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_bookmarks(corporation_id=None, _token=None)

   List corporation bookmarks

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: List of corporation owned bookmarks
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_bookmarks_folders(corporation_id=None, _token=None)

   List corporation bookmark folders

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: List of corporation owned bookmark folders
      :rtype: :class:`~esy.client.ESIPageGenerator` list




Calendar
--------

.. py:class:: Calendar

   .. py:method:: get_characters_character_id_calendar(character_id=None, [from_event=None], _token=None)

   List calendar event summaries

      :param int character_id: An EVE character ID
      :param int from_event: The event ID to retrieve events from
      :param str _token: ESI authorization token
      :return: A collection of event summaries
      :rtype: list


   .. py:method:: get_characters_character_id_calendar_event_id(character_id=None, event_id=None, _token=None)

   Get an event

      :param int character_id: An EVE character ID
      :param int event_id: The id of the event requested
      :param str _token: ESI authorization token
      :return: Full details of a specific event
      :rtype: dict


   .. py:method:: get_characters_character_id_calendar_event_id_attendees(character_id=None, event_id=None, _token=None)

   Get attendees

      :param int character_id: An EVE character ID
      :param int event_id: The id of the event requested
      :param str _token: ESI authorization token
      :return: List of attendees
      :rtype: list


   .. py:method:: put_characters_character_id_calendar_event_id(character_id=None, event_id=None, response=None, _token=None)

   Respond to an event

      :param int character_id: An EVE character ID
      :param int event_id: The ID of the event requested
      :param None response: The response value to set, overriding current value
      :param str _token: ESI authorization token
      :return: None
      :rtype: None




Character
---------

.. py:class:: Character

   .. py:method:: get_characters_character_id(character_id=None)

   Get character's public information

      :param int character_id: An EVE character ID
      :return: Public data for the given character
      :rtype: dict


   .. py:method:: get_characters_character_id_agents_research(character_id=None, _token=None)

   Get agents research

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of agents research information
      :rtype: list


   .. py:method:: get_characters_character_id_blueprints(character_id=None, _token=None)

   Get blueprints

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of blueprints
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_characters_character_id_corporationhistory(character_id=None)

   Get corporation history

      :param int character_id: An EVE character ID
      :return: Corporation history for the given character
      :rtype: list


   .. py:method:: get_characters_character_id_fatigue(character_id=None, _token=None)

   Get jump fatigue

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Jump activation and fatigue information
      :rtype: dict


   .. py:method:: get_characters_character_id_medals(character_id=None, _token=None)

   Get medals

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of medals
      :rtype: list


   .. py:method:: get_characters_character_id_notifications(character_id=None, _token=None)

   Get character notifications

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Returns your recent notifications
      :rtype: list


   .. py:method:: get_characters_character_id_notifications_contacts(character_id=None, _token=None)

   Get new contact notifications

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of contact notifications
      :rtype: list


   .. py:method:: get_characters_character_id_portrait(character_id=None)

   Get character portraits

      :param int character_id: An EVE character ID
      :return: Public data for the given character
      :rtype: dict


   .. py:method:: get_characters_character_id_roles(character_id=None, _token=None)

   Get character corporation roles

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: The character's roles in thier corporation
      :rtype: dict


   .. py:method:: get_characters_character_id_standings(character_id=None, _token=None)

   Get standings

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of standings
      :rtype: list


   .. py:method:: get_characters_character_id_stats(character_id=None, _token=None)

   Yearly aggregate stats

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Character stats
      :rtype: list


   .. py:method:: get_characters_character_id_titles(character_id=None, _token=None)

   Get character corporation titles

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of titles
      :rtype: list


   .. py:method:: post_characters_affiliation(characters=None)

   Character affiliation

      :param None characters: The character IDs to fetch affiliations for. All characters must exist, or none will be returned
      :return: Character corporation, alliance and faction IDs
      :rtype: list


   .. py:method:: post_characters_character_id_cspa(character_id=None, characters=None, _token=None)

   Calculate a CSPA charge cost

      :param int character_id: An EVE character ID
      :param None characters: The target characters to calculate the charge for
      :param str _token: ESI authorization token
      :return: None
      :rtype: None




Clones
------

.. py:class:: Clones

   .. py:method:: get_characters_character_id_clones(character_id=None, _token=None)

   Get clones

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Clone information for the given character
      :rtype: dict


   .. py:method:: get_characters_character_id_implants(character_id=None, _token=None)

   Get active implants

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of implant type ids
      :rtype: list




Contacts
--------

.. py:class:: Contacts

   .. py:method:: delete_characters_character_id_contacts(character_id=None, contact_ids=None, _token=None)

   Delete contacts

      :param int character_id: An EVE character ID
      :param list contact_ids: A list of contacts to delete
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: get_alliances_alliance_id_contacts(alliance_id=None, _token=None)

   Get alliance contacts

      :param int alliance_id: An EVE alliance ID
      :param str _token: ESI authorization token
      :return: A list of contacts
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_alliances_alliance_id_contacts_labels(alliance_id=None, _token=None)

   Get alliance contact labels

      :param int alliance_id: An EVE alliance ID
      :param str _token: ESI authorization token
      :return: A list of alliance contact labels
      :rtype: list


   .. py:method:: get_characters_character_id_contacts(character_id=None, _token=None)

   Get contacts

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of contacts
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_characters_character_id_contacts_labels(character_id=None, _token=None)

   Get contact labels

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of contact labels
      :rtype: list


   .. py:method:: get_corporations_corporation_id_contacts(corporation_id=None, _token=None)

   Get corporation contacts

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of contacts
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_contacts_labels(corporation_id=None, _token=None)

   Get corporation contact labels

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of corporation contact labels
      :rtype: list


   .. py:method:: post_characters_character_id_contacts(character_id=None, contact_ids=None, [label_ids=None], standing=None, [watched=False], _token=None)

   Add contacts

      :param int character_id: An EVE character ID
      :param None contact_ids: A list of contacts
      :param list label_ids: Add custom labels to the new contact
      :param number standing: Standing for the contact
      :param boolean watched: Whether the contact should be watched, note this is only effective on characters
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: put_characters_character_id_contacts(character_id=None, contact_ids=None, [label_ids=None], standing=None, [watched=False], _token=None)

   Edit contacts

      :param int character_id: An EVE character ID
      :param None contact_ids: A list of contacts
      :param list label_ids: Add custom labels to the contact
      :param number standing: Standing for the contact
      :param boolean watched: Whether the contact should be watched, note this is only effective on characters
      :param str _token: ESI authorization token
      :return: None
      :rtype: None




Contracts
---------

.. py:class:: Contracts

   .. py:method:: get_characters_character_id_contracts(character_id=None, _token=None)

   Get contracts

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of contracts
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_characters_character_id_contracts_contract_id_bids(character_id=None, contract_id=None, _token=None)

   Get contract bids

      :param int character_id: An EVE character ID
      :param int contract_id: ID of a contract
      :param str _token: ESI authorization token
      :return: A list of bids
      :rtype: list


   .. py:method:: get_characters_character_id_contracts_contract_id_items(character_id=None, contract_id=None, _token=None)

   Get contract items

      :param int character_id: An EVE character ID
      :param int contract_id: ID of a contract
      :param str _token: ESI authorization token
      :return: A list of items in this contract
      :rtype: list


   .. py:method:: get_contracts_public_bids_contract_id(contract_id=None)

   Get public contract bids

      :param int contract_id: ID of a contract
      :return: A list of bids
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_contracts_public_items_contract_id(contract_id=None)

   Get public contract items

      :param int contract_id: ID of a contract
      :return: A list of items in this contract
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_contracts_public_region_id(region_id=None)

   Get public contracts

      :param int region_id: An EVE region id
      :return: A list of contracts
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_contracts(corporation_id=None, _token=None)

   Get corporation contracts

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of contracts
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_contracts_contract_id_bids(contract_id=None, corporation_id=None, _token=None)

   Get corporation contract bids

      :param int contract_id: ID of a contract
      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of bids
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_contracts_contract_id_items(contract_id=None, corporation_id=None, _token=None)

   Get corporation contract items

      :param int contract_id: ID of a contract
      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of items in this contract
      :rtype: list




Corporation
-----------

.. py:class:: Corporation

   .. py:method:: get_corporations_corporation_id(corporation_id=None)

   Get corporation information

      :param int corporation_id: An EVE corporation ID
      :return: Public information about a corporation
      :rtype: dict


   .. py:method:: get_corporations_corporation_id_alliancehistory(corporation_id=None)

   Get alliance history

      :param int corporation_id: An EVE corporation ID
      :return: Alliance history for the given corporation
      :rtype: list


   .. py:method:: get_corporations_corporation_id_blueprints(corporation_id=None, _token=None)

   Get corporation blueprints

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: List of corporation blueprints
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_containers_logs(corporation_id=None, _token=None)

   Get all corporation ALSC logs

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: List of corporation ALSC logs
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_divisions(corporation_id=None, _token=None)

   Get corporation divisions

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: List of corporation division names
      :rtype: dict


   .. py:method:: get_corporations_corporation_id_facilities(corporation_id=None, _token=None)

   Get corporation facilities

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: List of corporation facilities
      :rtype: list


   .. py:method:: get_corporations_corporation_id_icons(corporation_id=None)

   Get corporation icon

      :param int corporation_id: An EVE corporation ID
      :return: Urls for icons for the given corporation id and server
      :rtype: dict


   .. py:method:: get_corporations_corporation_id_medals(corporation_id=None, _token=None)

   Get corporation medals

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of medals
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_medals_issued(corporation_id=None, _token=None)

   Get corporation issued medals

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of issued medals
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_members(corporation_id=None, _token=None)

   Get corporation members

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: List of member character IDs
      :rtype: list


   .. py:method:: get_corporations_corporation_id_members_limit(corporation_id=None, _token=None)

   Get corporation member limit

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: The corporation's member limit
      :rtype: int


   .. py:method:: get_corporations_corporation_id_members_titles(corporation_id=None, _token=None)

   Get corporation's members' titles

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of members and theirs titles
      :rtype: list


   .. py:method:: get_corporations_corporation_id_membertracking(corporation_id=None, _token=None)

   Track corporation members

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: List of member character IDs
      :rtype: list


   .. py:method:: get_corporations_corporation_id_roles(corporation_id=None, _token=None)

   Get corporation member roles

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: List of member character ID's and roles
      :rtype: list


   .. py:method:: get_corporations_corporation_id_roles_history(corporation_id=None, _token=None)

   Get corporation member roles history

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: List of role changes
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_shareholders(corporation_id=None, _token=None)

   Get corporation shareholders

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: List of shareholders
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_standings(corporation_id=None, _token=None)

   Get corporation standings

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of standings
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_starbases(corporation_id=None, _token=None)

   Get corporation starbases (POSes)

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: List of starbases (POSes)
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_starbases_starbase_id(corporation_id=None, starbase_id=None, system_id=None, _token=None)

   Get starbase (POS) detail

      :param int corporation_id: An EVE corporation ID
      :param int starbase_id: An EVE starbase (POS) ID
      :param int system_id: The solar system this starbase (POS) is located in,
      :param str _token: ESI authorization token
      :return: List of starbases (POSes)
      :rtype: dict


   .. py:method:: get_corporations_corporation_id_structures([Accept_Language='en-us'], corporation_id=None, [language='en-us'], _token=None)

   Get corporation structures

      :param str Accept_Language: Language to use in the response
      :param int corporation_id: An EVE corporation ID
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :param str _token: ESI authorization token
      :return: List of corporation structures' information
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_titles(corporation_id=None, _token=None)

   Get corporation titles

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of titles
      :rtype: list


   .. py:method:: get_corporations_npccorps()

   Get npc corporations

      :return: A list of npc corporation ids
      :rtype: list




Dogma
-----

.. py:class:: Dogma

   .. py:method:: get_dogma_attributes()

   Get attributes

      :return: A list of dogma attribute ids
      :rtype: list


   .. py:method:: get_dogma_attributes_attribute_id(attribute_id=None)

   Get attribute information

      :param int attribute_id: A dogma attribute ID
      :return: Information about a dogma attribute
      :rtype: dict


   .. py:method:: get_dogma_dynamic_items_type_id_item_id(item_id=None, type_id=None)

   Get dynamic item information

      :param int item_id: item_id integer
      :param int type_id: type_id integer
      :return: Details about a dynamic item
      :rtype: dict


   .. py:method:: get_dogma_effects()

   Get effects

      :return: A list of dogma effect ids
      :rtype: list


   .. py:method:: get_dogma_effects_effect_id(effect_id=None)

   Get effect information

      :param int effect_id: A dogma effect ID
      :return: Information about a dogma effect
      :rtype: dict




Faction_Warfare
---------------

.. py:class:: Faction_Warfare

   .. py:method:: get_characters_character_id_fw_stats(character_id=None, _token=None)

   Overview of a character involved in faction warfare

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Faction warfare statistics for a given character
      :rtype: dict


   .. py:method:: get_corporations_corporation_id_fw_stats(corporation_id=None, _token=None)

   Overview of a corporation involved in faction warfare

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: Faction warfare statistics for a given corporation
      :rtype: dict


   .. py:method:: get_fw_leaderboards()

   List of the top factions in faction warfare

      :return: Corporation leaderboard of kills and victory points within faction warfare
      :rtype: dict


   .. py:method:: get_fw_leaderboards_characters()

   List of the top pilots in faction warfare

      :return: Character leaderboard of kills and victory points within faction warfare
      :rtype: dict


   .. py:method:: get_fw_leaderboards_corporations()

   List of the top corporations in faction warfare

      :return: Corporation leaderboard of kills and victory points within faction warfare
      :rtype: dict


   .. py:method:: get_fw_stats()

   An overview of statistics about factions involved in faction warfare

      :return: Per faction breakdown of faction warfare statistics
      :rtype: list


   .. py:method:: get_fw_systems()

   Ownership of faction warfare systems

      :return: All faction warfare solar systems
      :rtype: list


   .. py:method:: get_fw_wars()

   Data about which NPC factions are at war

      :return: A list of NPC factions at war
      :rtype: list




Fittings
--------

.. py:class:: Fittings

   .. py:method:: delete_characters_character_id_fittings_fitting_id(character_id=None, fitting_id=None, _token=None)

   Delete fitting

      :param int character_id: An EVE character ID
      :param int fitting_id: ID for a fitting of this character
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: get_characters_character_id_fittings(character_id=None, _token=None)

   Get fittings

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of fittings
      :rtype: list


   .. py:method:: post_characters_character_id_fittings(character_id=None, fitting=None, _token=None)

   Create fitting

      :param int character_id: An EVE character ID
      :param None fitting: Details about the new fitting
      :param str _token: ESI authorization token
      :return: None
      :rtype: None




Fleets
------

.. py:class:: Fleets

   .. py:method:: delete_fleets_fleet_id_members_member_id(fleet_id=None, member_id=None, _token=None)

   Kick fleet member

      :param int fleet_id: ID for a fleet
      :param int member_id: The character ID of a member in this fleet
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: delete_fleets_fleet_id_squads_squad_id(fleet_id=None, squad_id=None, _token=None)

   Delete fleet squad

      :param int fleet_id: ID for a fleet
      :param int squad_id: The squad to delete
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: delete_fleets_fleet_id_wings_wing_id(fleet_id=None, wing_id=None, _token=None)

   Delete fleet wing

      :param int fleet_id: ID for a fleet
      :param int wing_id: The wing to delete
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: get_characters_character_id_fleet(character_id=None, _token=None)

   Get character fleet info

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Details about the character's fleet
      :rtype: dict


   .. py:method:: get_fleets_fleet_id(fleet_id=None, _token=None)

   Get fleet information

      :param int fleet_id: ID for a fleet
      :param str _token: ESI authorization token
      :return: Details about a fleet
      :rtype: dict


   .. py:method:: get_fleets_fleet_id_members([Accept_Language='en-us'], fleet_id=None, [language='en-us'], _token=None)

   Get fleet members

      :param str Accept_Language: Language to use in the response
      :param int fleet_id: ID for a fleet
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :param str _token: ESI authorization token
      :return: A list of fleet members
      :rtype: list


   .. py:method:: get_fleets_fleet_id_wings([Accept_Language='en-us'], fleet_id=None, [language='en-us'], _token=None)

   Get fleet wings

      :param str Accept_Language: Language to use in the response
      :param int fleet_id: ID for a fleet
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :param str _token: ESI authorization token
      :return: A list of fleet wings
      :rtype: list


   .. py:method:: post_fleets_fleet_id_members(fleet_id=None, invitation=None, _token=None)

   Create fleet invitation

      :param int fleet_id: ID for a fleet
      :param None invitation: Details of the invitation
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: post_fleets_fleet_id_wings(fleet_id=None, _token=None)

   Create fleet wing

      :param int fleet_id: ID for a fleet
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: post_fleets_fleet_id_wings_wing_id_squads(fleet_id=None, wing_id=None, _token=None)

   Create fleet squad

      :param int fleet_id: ID for a fleet
      :param int wing_id: The wing_id to create squad in
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: put_fleets_fleet_id(fleet_id=None, new_settings=None, _token=None)

   Update fleet

      :param int fleet_id: ID for a fleet
      :param None new_settings: What to update for this fleet
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: put_fleets_fleet_id_members_member_id(fleet_id=None, member_id=None, movement=None, _token=None)

   Move fleet member

      :param int fleet_id: ID for a fleet
      :param int member_id: The character ID of a member in this fleet
      :param None movement: Details of the invitation
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: put_fleets_fleet_id_squads_squad_id(fleet_id=None, naming=None, squad_id=None, _token=None)

   Rename fleet squad

      :param int fleet_id: ID for a fleet
      :param None naming: New name of the squad
      :param int squad_id: The squad to rename
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: put_fleets_fleet_id_wings_wing_id(fleet_id=None, naming=None, wing_id=None, _token=None)

   Rename fleet wing

      :param int fleet_id: ID for a fleet
      :param None naming: New name of the wing
      :param int wing_id: The wing to rename
      :param str _token: ESI authorization token
      :return: None
      :rtype: None




Incursions
----------

.. py:class:: Incursions

   .. py:method:: get_incursions()

   List incursions

      :return: A list of incursions
      :rtype: list




Industry
--------

.. py:class:: Industry

   .. py:method:: get_characters_character_id_industry_jobs(character_id=None, [include_completed=None], _token=None)

   List character industry jobs

      :param int character_id: An EVE character ID
      :param boolean include_completed: Whether to retrieve completed character industry jobs. Only includes jobs from the past 90 days
      :param str _token: ESI authorization token
      :return: Industry jobs placed by a character
      :rtype: list


   .. py:method:: get_characters_character_id_mining(character_id=None, _token=None)

   Character mining ledger

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Mining ledger of a character
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporation_corporation_id_mining_extractions(corporation_id=None, _token=None)

   Moon extraction timers

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of chunk timers
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporation_corporation_id_mining_observers(corporation_id=None, _token=None)

   Corporation mining observers

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: Observer list of a corporation
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporation_corporation_id_mining_observers_observer_id(corporation_id=None, observer_id=None, _token=None)

   Observed corporation mining

      :param int corporation_id: An EVE corporation ID
      :param int observer_id: A mining observer id
      :param str _token: ESI authorization token
      :return: Mining ledger of an observer
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_industry_jobs(corporation_id=None, [include_completed=False], _token=None)

   List corporation industry jobs

      :param int corporation_id: An EVE corporation ID
      :param boolean include_completed: Whether to retrieve completed corporation industry jobs. Only includes jobs from the past 90 days
      :param str _token: ESI authorization token
      :return: A list of corporation industry jobs
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_industry_facilities()

   List industry facilities

      :return: A list of facilities
      :rtype: list


   .. py:method:: get_industry_systems()

   List solar system cost indices

      :return: A list of cost indicies
      :rtype: list




Insurance
---------

.. py:class:: Insurance

   .. py:method:: get_insurance_prices([Accept_Language='en-us'], [language='en-us'])

   List insurance levels

      :param str Accept_Language: Language to use in the response
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :return: A list of insurance levels for all ship types
      :rtype: list




Killmails
---------

.. py:class:: Killmails

   .. py:method:: get_characters_character_id_killmails_recent(character_id=None, _token=None)

   Get a character's recent kills and losses

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of killmail IDs and hashes
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_killmails_recent(corporation_id=None, _token=None)

   Get a corporation's recent kills and losses

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of killmail IDs and hashes
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_killmails_killmail_id_killmail_hash(killmail_hash=None, killmail_id=None)

   Get a single killmail

      :param str killmail_hash: The killmail hash for verification
      :param int killmail_id: The killmail ID to be queried
      :return: A killmail
      :rtype: dict




Location
--------

.. py:class:: Location

   .. py:method:: get_characters_character_id_location(character_id=None, _token=None)

   Get character location

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Information about the characters current location. Returns the current solar system id, and also the current station or structure ID if applicable
      :rtype: dict


   .. py:method:: get_characters_character_id_online(character_id=None, _token=None)

   Get character online

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Object describing the character's online status
      :rtype: dict


   .. py:method:: get_characters_character_id_ship(character_id=None, _token=None)

   Get current ship

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Get the current ship type, name and id
      :rtype: dict




Loyalty
-------

.. py:class:: Loyalty

   .. py:method:: get_characters_character_id_loyalty_points(character_id=None, _token=None)

   Get loyalty points

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of loyalty points
      :rtype: list


   .. py:method:: get_loyalty_stores_corporation_id_offers(corporation_id=None)

   List loyalty store offers

      :param int corporation_id: An EVE corporation ID
      :return: A list of offers
      :rtype: list




Mail
----

.. py:class:: Mail

   .. py:method:: delete_characters_character_id_mail_labels_label_id(character_id=None, label_id=None, _token=None)

   Delete a mail label

      :param int character_id: An EVE character ID
      :param int label_id: An EVE label id
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: delete_characters_character_id_mail_mail_id(character_id=None, mail_id=None, _token=None)

   Delete a mail

      :param int character_id: An EVE character ID
      :param int mail_id: An EVE mail ID
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: get_characters_character_id_mail(character_id=None, [labels=None], [last_mail_id=None], _token=None)

   Return mail headers

      :param int character_id: An EVE character ID
      :param list labels: Fetch only mails that match one or more of the given labels
      :param int last_mail_id: List only mail with an ID lower than the given ID, if present
      :param str _token: ESI authorization token
      :return: The requested mail
      :rtype: list


   .. py:method:: get_characters_character_id_mail_labels(character_id=None, _token=None)

   Get mail labels and unread counts

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of mail labels and unread counts
      :rtype: dict


   .. py:method:: get_characters_character_id_mail_lists(character_id=None, _token=None)

   Return mailing list subscriptions

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Mailing lists
      :rtype: list


   .. py:method:: get_characters_character_id_mail_mail_id(character_id=None, mail_id=None, _token=None)

   Return a mail

      :param int character_id: An EVE character ID
      :param int mail_id: An EVE mail ID
      :param str _token: ESI authorization token
      :return: Contents of a mail
      :rtype: dict


   .. py:method:: post_characters_character_id_mail(character_id=None, mail=None, _token=None)

   Send a new mail

      :param int character_id: An EVE character ID
      :param None mail: The mail to send
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: post_characters_character_id_mail_labels(character_id=None, label=None, _token=None)

   Create a mail label

      :param int character_id: An EVE character ID
      :param None label: Label to create
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: put_characters_character_id_mail_mail_id(character_id=None, contents=None, mail_id=None, _token=None)

   Update metadata about a mail

      :param int character_id: An EVE character ID
      :param None contents: Data used to update the mail
      :param int mail_id: An EVE mail ID
      :param str _token: ESI authorization token
      :return: None
      :rtype: None




Market
------

.. py:class:: Market

   .. py:method:: get_characters_character_id_orders(character_id=None, _token=None)

   List open orders from a character

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Open market orders placed by a character
      :rtype: list


   .. py:method:: get_characters_character_id_orders_history(character_id=None, _token=None)

   List historical orders by a character

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Expired and cancelled market orders placed by a character
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_orders(corporation_id=None, _token=None)

   List open orders from a corporation

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of open market orders
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_orders_history(corporation_id=None, _token=None)

   List historical orders from a corporation

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: Expired and cancelled market orders placed on behalf of a corporation
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_markets_groups()

   Get item groups

      :return: A list of item group ids
      :rtype: list


   .. py:method:: get_markets_groups_market_group_id([Accept_Language='en-us'], [language='en-us'], market_group_id=None)

   Get item group information

      :param str Accept_Language: Language to use in the response
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :param int market_group_id: An Eve item group ID
      :return: Information about an item group
      :rtype: dict


   .. py:method:: get_markets_prices()

   List market prices

      :return: A list of prices
      :rtype: list


   .. py:method:: get_markets_region_id_history(region_id=None, type_id=None)

   List historical market statistics in a region

      :param int region_id: Return statistics in this region
      :param int type_id: Return statistics for this type
      :return: A list of historical market statistics
      :rtype: list


   .. py:method:: get_markets_region_id_orders(order_type=None, region_id=None, [type_id=None])

   List orders in a region

      :param str order_type: Filter buy/sell orders, return all orders by default. If you query without type_id, we always return both buy and sell orders
      :param int region_id: Return orders in this region
      :param int type_id: Return orders only for this type
      :return: A list of orders
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_markets_region_id_types(region_id=None)

   List type IDs relevant to a market

      :param int region_id: Return statistics in this region
      :return: A list of type IDs
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_markets_structures_structure_id(structure_id=None, _token=None)

   List orders in a structure

      :param int structure_id: Return orders in this structure
      :param str _token: ESI authorization token
      :return: A list of orders
      :rtype: :class:`~esy.client.ESIPageGenerator` list




Opportunities
-------------

.. py:class:: Opportunities

   .. py:method:: get_characters_character_id_opportunities(character_id=None, _token=None)

   Get a character's completed tasks

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: A list of opportunities task ids
      :rtype: list


   .. py:method:: get_opportunities_groups()

   Get opportunities groups

      :return: A list of opportunities group ids
      :rtype: list


   .. py:method:: get_opportunities_groups_group_id([Accept_Language='en-us'], group_id=None, [language='en-us'])

   Get opportunities group

      :param str Accept_Language: Language to use in the response
      :param int group_id: ID of an opportunities group
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :return: Details of an opportunities group
      :rtype: dict


   .. py:method:: get_opportunities_tasks()

   Get opportunities tasks

      :return: A list of opportunities task ids
      :rtype: list


   .. py:method:: get_opportunities_tasks_task_id(task_id=None)

   Get opportunities task

      :param int task_id: ID of an opportunities task
      :return: Details of an opportunities task
      :rtype: dict




Planetary_Interaction
---------------------

.. py:class:: Planetary_Interaction

   .. py:method:: get_characters_character_id_planets(character_id=None, _token=None)

   Get colonies

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: List of colonies
      :rtype: list


   .. py:method:: get_characters_character_id_planets_planet_id(character_id=None, planet_id=None, _token=None)

   Get colony layout

      :param int character_id: An EVE character ID
      :param int planet_id: Planet id of the target planet
      :param str _token: ESI authorization token
      :return: Colony layout
      :rtype: dict


   .. py:method:: get_corporations_corporation_id_customs_offices(corporation_id=None, _token=None)

   List corporation customs offices

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: A list of customs offices and their settings
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_universe_schematics_schematic_id(schematic_id=None)

   Get schematic information

      :param int schematic_id: A PI schematic ID
      :return: Public data about a schematic
      :rtype: dict




Routes
------

.. py:class:: Routes

   .. py:method:: get_route_origin_destination([avoid=None], [connections=None], destination=None, [flag='shortest'], origin=None)

   Get route

      :param list avoid: avoid solar system ID(s)
      :param list connections: connected solar system pairs
      :param int destination: destination solar system ID
      :param str flag: route security preference
      :param int origin: origin solar system ID
      :return: Solar systems in route from origin to destination
      :rtype: list




Search
------

.. py:class:: Search

   .. py:method:: get_characters_character_id_search([Accept_Language='en-us'], categories=None, character_id=None, [language='en-us'], search=None, [strict=False], _token=None)

   Search on a string

      :param str Accept_Language: Language to use in the response
      :param list categories: Type of entities to search for
      :param int character_id: An EVE character ID
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :param str search: The string to search on
      :param boolean strict: Whether the search should be a strict match
      :param str _token: ESI authorization token
      :return: A list of search results
      :rtype: dict


   .. py:method:: get_search([Accept_Language='en-us'], categories=None, [language='en-us'], search=None, [strict=False])

   Search on a string

      :param str Accept_Language: Language to use in the response
      :param list categories: Type of entities to search for
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :param str search: The string to search on
      :param boolean strict: Whether the search should be a strict match
      :return: A list of search results
      :rtype: dict




Skills
------

.. py:class:: Skills

   .. py:method:: get_characters_character_id_attributes(character_id=None, _token=None)

   Get character attributes

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Attributes of a character
      :rtype: dict


   .. py:method:: get_characters_character_id_skillqueue(character_id=None, _token=None)

   Get character's skill queue

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: The current skill queue, sorted ascending by finishing time
      :rtype: list


   .. py:method:: get_characters_character_id_skills(character_id=None, _token=None)

   Get character skills

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Known skills for the character
      :rtype: dict




Sovereignty
-----------

.. py:class:: Sovereignty

   .. py:method:: get_sovereignty_campaigns()

   List sovereignty campaigns

      :return: A list of sovereignty campaigns
      :rtype: list


   .. py:method:: get_sovereignty_map()

   List sovereignty of systems

      :return: A list of sovereignty information for solar systems in New Eden
      :rtype: list


   .. py:method:: get_sovereignty_structures()

   List sovereignty structures

      :return: A list of sovereignty structures
      :rtype: list




Status
------

.. py:class:: Status

   .. py:method:: get_status()

   Retrieve the uptime and player counts

      :return: Server status
      :rtype: dict




Universe
--------

.. py:class:: Universe

   .. py:method:: get_universe_ancestries([Accept_Language='en-us'], [language='en-us'])

   Get ancestries

      :param str Accept_Language: Language to use in the response
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :return: A list of ancestries
      :rtype: list


   .. py:method:: get_universe_asteroid_belts_asteroid_belt_id(asteroid_belt_id=None)

   Get asteroid belt information

      :param int asteroid_belt_id: asteroid_belt_id integer
      :return: Information about an asteroid belt
      :rtype: dict


   .. py:method:: get_universe_bloodlines([Accept_Language='en-us'], [language='en-us'])

   Get bloodlines

      :param str Accept_Language: Language to use in the response
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :return: A list of bloodlines
      :rtype: list


   .. py:method:: get_universe_categories()

   Get item categories

      :return: A list of item category ids
      :rtype: list


   .. py:method:: get_universe_categories_category_id([Accept_Language='en-us'], category_id=None, [language='en-us'])

   Get item category information

      :param str Accept_Language: Language to use in the response
      :param int category_id: An Eve item category ID
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :return: Information about an item category
      :rtype: dict


   .. py:method:: get_universe_constellations()

   Get constellations

      :return: A list of constellation ids
      :rtype: list


   .. py:method:: get_universe_constellations_constellation_id([Accept_Language='en-us'], constellation_id=None, [language='en-us'])

   Get constellation information

      :param str Accept_Language: Language to use in the response
      :param int constellation_id: constellation_id integer
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :return: Information about a constellation
      :rtype: dict


   .. py:method:: get_universe_factions([Accept_Language='en-us'], [language='en-us'])

   Get factions

      :param str Accept_Language: Language to use in the response
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :return: A list of factions
      :rtype: list


   .. py:method:: get_universe_graphics()

   Get graphics

      :return: A list of graphic ids
      :rtype: list


   .. py:method:: get_universe_graphics_graphic_id(graphic_id=None)

   Get graphic information

      :param int graphic_id: graphic_id integer
      :return: Information about a graphic
      :rtype: dict


   .. py:method:: get_universe_groups()

   Get item groups

      :return: A list of item group ids
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_universe_groups_group_id([Accept_Language='en-us'], group_id=None, [language='en-us'])

   Get item group information

      :param str Accept_Language: Language to use in the response
      :param int group_id: An Eve item group ID
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :return: Information about an item group
      :rtype: dict


   .. py:method:: get_universe_moons_moon_id(moon_id=None)

   Get moon information

      :param int moon_id: moon_id integer
      :return: Information about a moon
      :rtype: dict


   .. py:method:: get_universe_planets_planet_id(planet_id=None)

   Get planet information

      :param int planet_id: planet_id integer
      :return: Information about a planet
      :rtype: dict


   .. py:method:: get_universe_races([Accept_Language='en-us'], [language='en-us'])

   Get character races

      :param str Accept_Language: Language to use in the response
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :return: A list of character races
      :rtype: list


   .. py:method:: get_universe_regions()

   Get regions

      :return: A list of region ids
      :rtype: list


   .. py:method:: get_universe_regions_region_id([Accept_Language='en-us'], [language='en-us'], region_id=None)

   Get region information

      :param str Accept_Language: Language to use in the response
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :param int region_id: region_id integer
      :return: Information about a region
      :rtype: dict


   .. py:method:: get_universe_stargates_stargate_id(stargate_id=None)

   Get stargate information

      :param int stargate_id: stargate_id integer
      :return: Information about a stargate
      :rtype: dict


   .. py:method:: get_universe_stars_star_id(star_id=None)

   Get star information

      :param int star_id: star_id integer
      :return: Information about a star
      :rtype: dict


   .. py:method:: get_universe_stations_station_id(station_id=None)

   Get station information

      :param int station_id: station_id integer
      :return: Information about a station
      :rtype: dict


   .. py:method:: get_universe_structures([filter=None])

   List all public structures

      :param str filter: Only list public structures that have this service online
      :return: List of public structure IDs
      :rtype: list


   .. py:method:: get_universe_structures_structure_id(structure_id=None, _token=None)

   Get structure information

      :param int structure_id: An Eve structure ID
      :param str _token: ESI authorization token
      :return: Data about a structure
      :rtype: dict


   .. py:method:: get_universe_system_jumps()

   Get system jumps

      :return: A list of systems and number of jumps
      :rtype: list


   .. py:method:: get_universe_system_kills()

   Get system kills

      :return: A list of systems and number of ship, pod and NPC kills
      :rtype: list


   .. py:method:: get_universe_systems()

   Get solar systems

      :return: A list of solar system ids
      :rtype: list


   .. py:method:: get_universe_systems_system_id([Accept_Language='en-us'], [language='en-us'], system_id=None)

   Get solar system information

      :param str Accept_Language: Language to use in the response
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :param int system_id: system_id integer
      :return: Information about a solar system
      :rtype: dict


   .. py:method:: get_universe_types()

   Get types

      :return: A list of type ids
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_universe_types_type_id([Accept_Language='en-us'], [language='en-us'], type_id=None)

   Get type information

      :param str Accept_Language: Language to use in the response
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :param int type_id: An Eve item type ID
      :return: Information about a type
      :rtype: dict


   .. py:method:: post_universe_ids([Accept_Language='en-us'], [language='en-us'], names=None)

   Bulk names to IDs

      :param str Accept_Language: Language to use in the response
      :param str language: Language to use in the response, takes precedence over Accept-Language
      :param None names: The names to resolve
      :return: List of id/name associations for a set of names divided by category. Any name passed in that did not have a match will be ommitted
      :rtype: dict


   .. py:method:: post_universe_names(ids=None)

   Get names and categories for a set of IDs

      :param None ids: The ids to resolve
      :return: List of id/name associations for a set of IDs. All IDs must resolve to a name, or nothing will be returned
      :rtype: list




User_Interface
--------------

.. py:class:: User_Interface

   .. py:method:: post_ui_autopilot_waypoint(add_to_beginning=None, clear_other_waypoints=None, destination_id=None, _token=None)

   Set Autopilot Waypoint

      :param boolean add_to_beginning: Whether this solar system should be added to the beginning of all waypoints
      :param boolean clear_other_waypoints: Whether clean other waypoints beforing adding this one
      :param int destination_id: The destination to travel to, can be solar system, station or structure's id
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: post_ui_openwindow_contract(contract_id=None, _token=None)

   Open Contract Window

      :param int contract_id: The contract to open
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: post_ui_openwindow_information(target_id=None, _token=None)

   Open Information Window

      :param int target_id: The target to open
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: post_ui_openwindow_marketdetails(type_id=None, _token=None)

   Open Market Details

      :param int type_id: The item type to open in market window
      :param str _token: ESI authorization token
      :return: None
      :rtype: None


   .. py:method:: post_ui_openwindow_newmail(new_mail=None, _token=None)

   Open New Mail Window

      :param None new_mail: The details of mail to create
      :param str _token: ESI authorization token
      :return: None
      :rtype: None




Wallet
------

.. py:class:: Wallet

   .. py:method:: get_characters_character_id_wallet(character_id=None, _token=None)

   Get a character's wallet balance

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Wallet balance
      :rtype: number


   .. py:method:: get_characters_character_id_wallet_journal(character_id=None, _token=None)

   Get character wallet journal

      :param int character_id: An EVE character ID
      :param str _token: ESI authorization token
      :return: Journal entries
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_characters_character_id_wallet_transactions(character_id=None, [from_id=None], _token=None)

   Get wallet transactions

      :param int character_id: An EVE character ID
      :param int from_id: Only show transactions happened before the one referenced by this id
      :param str _token: ESI authorization token
      :return: Wallet transactions
      :rtype: list


   .. py:method:: get_corporations_corporation_id_wallets(corporation_id=None, _token=None)

   Returns a corporation's wallet balance

      :param int corporation_id: An EVE corporation ID
      :param str _token: ESI authorization token
      :return: List of corporation wallets
      :rtype: list


   .. py:method:: get_corporations_corporation_id_wallets_division_journal(corporation_id=None, division=None, _token=None)

   Get corporation wallet journal

      :param int corporation_id: An EVE corporation ID
      :param int division: Wallet key of the division to fetch journals from
      :param str _token: ESI authorization token
      :return: Journal entries
      :rtype: :class:`~esy.client.ESIPageGenerator` list


   .. py:method:: get_corporations_corporation_id_wallets_division_transactions(corporation_id=None, division=None, [from_id=None], _token=None)

   Get corporation wallet transactions

      :param int corporation_id: An EVE corporation ID
      :param int division: Wallet key of the division to fetch journals from
      :param int from_id: Only show journal entries happened before the transaction referenced by this id
      :param str _token: ESI authorization token
      :return: Wallet transactions
      :rtype: list




Wars
----

.. py:class:: Wars

   .. py:method:: get_wars([max_war_id=None])

   List wars

      :param int max_war_id: Only return wars with ID smaller than this
      :return: A list of war IDs, in descending order by war_id
      :rtype: list


   .. py:method:: get_wars_war_id(war_id=None)

   Get war information

      :param int war_id: ID for a war
      :return: Details about a war
      :rtype: dict


   .. py:method:: get_wars_war_id_killmails(war_id=None)

   List kills for a war

      :param int war_id: A valid war ID
      :return: A list of killmail IDs and hashes
      :rtype: :class:`~esy.client.ESIPageGenerator` list




