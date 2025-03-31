/**
 * Full set of knob skins from react-rotary-knob-skin-pack
 * Implementation adapted for Dash compatibility
 */

// Import all available skins
import s1 from './skins/s1';
import s2 from './skins/s2';
import s3 from './skins/s3';
import s4 from './skins/s4';
import s5 from './skins/s5';
import s6 from './skins/s6';
import s7 from './skins/s7';
import s8 from './skins/s8';
import s9 from './skins/s9';
import s10 from './skins/s10';
import s11 from './skins/s11';
import s12 from './skins/s12';
import s13 from './skins/s13';
import s14 from './skins/s14';
import s15 from './skins/s15';
import s16 from './skins/s16';
import s17 from './skins/s17';
import s18 from './skins/s18';

// Map of all available skins
const skins = {
  s1,
  s2,
  s3,
  s4,
  s5,
  s6,
  s7,
  s8,
  s9,
  s10,
  s11,
  s12,
  s13,
  s14,
  s15,
  s16,
  s17,
  s18,
  default: s1
};

// Default skin
const defaultSkin = skins.s1;

// Helper to get a skin by name with fallback to default
const getSkin = (skinName) => {
  return skins[skinName] || defaultSkin;
};

export {
  skins,
  defaultSkin,
  getSkin
};