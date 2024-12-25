import { I18n } from "i18n-js";
import * as Localization from "expo-localization";
import en from "@/assets/translations/en.json";
import fr from "@/assets/translations/fr.json";
import ar from "@/assets/translations/ar.json";

const i18n = new I18n({
  ...ar,
  ...fr,
  ...en,
});

i18n.defaultLocale = "fr";
i18n.locale = Localization.getLocales()[0].languageCode ?? "fr";
i18n.enableFallback = true;

export default i18n;
