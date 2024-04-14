<template>
  <v-navigation-drawer
    permanent
    width="238"
    class="primary navigation-shadow"
    style="z-index: 11 !important"
    dark
    clipped
    app
    mini-variant
    expand-on-hover
  >
    <v-list dense>
      <v-list-item v-for="(item, i) in navMenu" :key="i" class="pa-0 ma-0">
        <v-list-group
          v-if="item && item.items && item.items.length > 0"
          class="w-100 v-list-sub-group white--text"
        >
          <template v-slot:activator>
            <v-list-item
              class="border-bottom-light_maroon"
              router
              exact
              :to="item.to"
            >
              <v-list-item-action class="mr-2">
                <v-icon class="text-h6 font-weight-light">
                  {{ item.icon }}
                </v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title style="text-transform: capitalize">
                  {{ item.title }}
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </template>

          <v-list-item
            class="border-bottom-light_maroon background-blue"
            router
            exact
            v-for="(subItem, index) in item.items"
            :key="index"
            :to="subItem.to"
          >
            <v-list-item-action class="mr-2">
              <v-icon class="text-h6 font-weight-light">
                {{ subItem.icon }}
              </v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title style="text-transform: capitalize">
                {{ subItem.title }}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>

        <v-list-item
          v-else
          class="border-bottom-light_maroon"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action class="mr-2">
            <v-icon class="text-h6 font-weight-light">{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title style="text-transform: capitalize">
              {{ item.title }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
/* eslint-disable vue/no-unused-components */
export default {
  data() {
    return {
      // permission: JSON.parse(localStorage.getItem("permissions")),
      clientMenu: [
        {
          title: "dashboard",
          icon: "mdi-monitor-dashboard",
          to: "/app/client/dashboard",
          key: "user",
        },
        {
          title: "slots",
          icon: "mdi-archive-outline",
          to: "/app/client/slots",
          key: "user",
        },
      ],
      adminMenu: [
        {
          title: "dashboard",
          icon: "mdi-monitor-dashboard",
          to: "/app/admin/dashboard",
          key: "user",
        },
        {
          title: "slots",
          icon: "mdi-archive-outline",
          to: "/app/admin/fixed_slots",
          key: "user",
        },
        {
          title: "plots",
          icon: "mdi-parking",
          to: "/app/admin/plots",
          key: "user",
        },
        {
          title: "users",
          icon: "mdi-account-plus",
          to: "/app/admin/users",
          key: "user",
        }
      ],
    };
  },
  computed: {
    navMenu() {
      const user_detail = JSON.parse(localStorage.getItem("user_detail"));
      if (user_detail["user_type"] == "admin") {
        return this.adminMenu.filter((obj) => {
          if (obj.key) {
            return true;
          } else {
            if (obj.items && obj.items.length > 0) {
              obj.items = obj.items.filter((subMenu) => {
                if (subMenu.key) {
                  return true;
                } else {
                  return false;
                }
              });
            }
            if (obj.items && obj.items.length > 0) {
              return true;
            } else {
              return false;
            }
          }
        });
      } else {
        return this.clientMenu.filter((obj) => {
          if (obj.key) {
            return true;
          } else {
            if (obj.items && obj.items.length > 0) {
              obj.items = obj.items.filter((subMenu) => {
                if (subMenu.key) {
                  return true;
                } else {
                  return false;
                }
              });
            }
            if (obj.items && obj.items.length > 0) {
              return true;
            } else {
              return false;
            }
          }
        });
      }
    },
  },
  mounted() {},
};
</script>

<style lang="scss">
.v-list-sub-group .border-bottom-light_maroon {
  border: none !important;
}
.v-list-sub-group .v-list-group__header {
  border-bottom: 1px solid #122d4e !important;
}
.navigation-shadow {
  &:hover {
    box-shadow: black 4px 0px 20px -10px !important;
  }
}
.v-list-sub-group {
  .v-list-group__header {
    padding: 0 !important;
  }
}
</style>
