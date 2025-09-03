<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BRAKO - نظام إدارة الشحنات</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');
        body { font-family: 'Cairo', sans-serif; }
        .gradient-bg { background: linear-gradient(135deg, #1e40af 0%, #14b8a6 50%, #fbbf24 100%); }
        .section-content { animation: fadeIn 0.5s ease-in-out; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        .modal { transition: opacity 0.3s ease, visibility 0.3s ease; }
        .tooltip .tooltip-text { visibility: hidden; width: 120px; background-color: #333; color: #fff; text-align: center; border-radius: 6px; padding: 5px 0; position: absolute; z-index: 1; bottom: 125%; right: 50%; transform: translateX(50%); opacity: 0; transition: opacity 0.3s; }
        .tooltip:hover .tooltip-text { visibility: visible; opacity: 1; }
    </style>
</head>
<body class="bg-gray-50">
    <!-- Header -->
    <header class="gradient-bg text-white shadow-lg sticky top-0 z-50">
        <div class="container mx-auto px-4 py-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center space-x-4 space-x-reverse">
                    <div class="bg-white text-brako-blue px-4 py-2 rounded-lg font-bold text-2xl">BRAKO</div>
                    <span class="text-xl font-semibold">شركة الشحن الدولي</span>
                </div>
                <!-- زر القائمة (يظهر على الشاشات الصغيرة فقط) -->
                <button id="mobile-menu-btn" class="md:hidden text-white text-2xl" onclick="toggleMobileMenu()">
                    ☰
                </button>
                <div class="flex-grow"></div>
                <!-- قائمة التنقل (مخفية على الشاشات الصغيرة وتظهر على الكبيرة) -->
                <nav id="main-nav" class="hidden md:flex space-x-6 space-x-reverse">
                    <a href="#" class="hover:text-brako-yellow transition-colors cursor-pointer" onclick="showSection('home')">الصفحة الرئيسية</a>
                    <a href="#" class="hover:text-brako-yellow transition-colors cursor-pointer" onclick="showSection('services')">خدماتنا</a>
                    <a href="#" class="hover:text-brako-yellow transition-colors cursor-pointer" onclick="showSection('about')">من نحن</a>
                    <a href="#" class="hover:text-brako-yellow transition-colors cursor-pointer" onclick="showSection('contact')">تواصل معنا</a>
                    <a href="#" class="hover:text-brako-yellow transition-colors cursor-pointer" onclick="showSection('customerTracking')">تتبع الشحنة</a>
                    <button id="admin-btn" onclick="showSection('admin')" class="bg-brako-yellow text-brako-blue px-4 py-2 rounded-lg font-semibold hover:bg-yellow-300 transition-colors">إدارة الشحنات</button>
                </nav>
            </div>
            <!-- قائمة التنقل الخاصة بالهواتف (تظهر عند الضغط على زر القائمة) -->
            <div id="mobile-menu" class="hidden md:hidden mt-4 space-y-2">
                <a href="#" class="block px-4 py-2 text-sm text-white hover:bg-white hover:bg-opacity-20 rounded-lg" onclick="showSection('home'); toggleMobileMenu()">الصفحة الرئيسية</a>
                <a href="#" class="block px-4 py-2 text-sm text-white hover:bg-white hover:bg-opacity-20 rounded-lg" onclick="showSection('services'); toggleMobileMenu()">خدماتنا</a>
                <a href="#" class="block px-4 py-2 text-sm text-white hover:bg-white hover:bg-opacity-20 rounded-lg" onclick="showSection('about'); toggleMobileMenu()">من نحن</a>
                <a href="#" class="block px-4 py-2 text-sm text-white hover:bg-white hover:bg-opacity-20 rounded-lg" onclick="showSection('contact'); toggleMobileMenu()">تواصل معنا</a>
                <a href="#" class="block px-4 py-2 text-sm text-white hover:bg-white hover:bg-opacity-20 rounded-lg" onclick="showSection('customerTracking'); toggleMobileMenu()">تتبع الشحنة</a>
                <button onclick="showSection('admin'); toggleMobileMenu()" class="block w-full text-right bg-brako-yellow text-brako-blue px-4 py-2 rounded-lg font-semibold hover:bg-yellow-300 transition-colors">إدارة الشحنات</button>
            </div>
        </div>
    </header>

    <!-- الرئيسية -->
    <section id="home" class="section-content">
        <div class="gradient-bg text-white py-20">
            <div class="container mx-auto px-4 text-center">
                <h1 class="text-5xl font-bold mb-6">مرحباً بكم في BRAKO</h1>
                <p class="text-xl mb-8">شركة الشحن الدولي الرائدة - خدمات شحن موثوقة وسريعة</p>
                <button onclick="showSection('admin')" class="bg-brako-yellow text-brako-blue px-8 py-4 rounded-lg text-lg font-semibold hover:bg-yellow-300 transition-colors">
                    إدارة الشحنات
                </button>
            </div>
        </div>
        
        <!-- إحصائيات الشركة -->
        <div class="container mx-auto px-4 py-8">
            <div id="statistics-cards" class="grid md:grid-cols-4 gap-6 mb-12">
                <!-- Cards will be populated dynamically -->
                <div class="bg-white p-6 rounded-lg shadow-lg text-center border-r-4 border-brako-blue">
                    <div class="text-3xl font-bold text-brako-blue mb-2" id="totalShipments">0</div>
                    <p class="text-gray-600">إجمالي الشحنات</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg text-center border-r-4 border-brako-teal">
                    <div class="text-3xl font-bold text-brako-teal mb-2" id="totalRevenue">0</div>
                    <p class="text-gray-600">إجمالي الإيرادات</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg text-center border-r-4 border-green-500">
                    <div class="text-3xl font-bold text-green-500 mb-2" id="deliveredShipments">0</div>
                    <p class="text-gray-600">الشحنات المسلمة</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg text-center border-r-4 border-brako-yellow">
                    <div class="text-3xl font-bold text-brako-yellow mb-2" id="pendingShipments">0</div>
                    <p class="text-gray-600">الشحنات قيد التنفيذ</p>
                </div>
            </div>
            <div class="grid md:grid-cols-3 gap-8">
                 
                <div class="bg-white p-6 rounded-lg shadow-lg text-center">
                    <div class="bg-brako-blue text-white w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 text-2xl">🚚</div>
                    <h3 class="text-xl font-semibold mb-2">شحن سريع</h3>
                    <p class="text-gray-600">خدمات شحن سريعة وموثوقة لجميع أنحاء العالم</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg text-center">
                    <div class="bg-brako-teal text-white w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 text-2xl">📦</div>
                    <h3 class="text-xl font-semibold mb-2">تغليف آمن</h3>
                    <p class="text-gray-600">تغليف احترافي يضمن وصول شحنتك بأمان</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg text-center">
                    <div class="bg-brako-yellow text-white w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 text-2xl">🛡️</div>
                    <h3 class="text-xl font-semibold mb-2">تأمين شامل</h3>
                    <p class="text-gray-600">خدمات تأمين شاملة لحماية شحناتك</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="section-content hidden">
        <div class="container mx-auto px-4 py-16">
            <h2 class="text-4xl font-bold text-center mb-12 text-brako-blue">خدماتنا</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="bg-white p-8 rounded-lg shadow-lg">
                    <h3 class="text-2xl font-semibold mb-4 text-brako-teal">الشحن الدولي</h3>
                    <ul class="space-y-2 text-gray-700">
                        <li>• شحن جوي سريع</li>
                        <li>• شحن بري للدول المجاورة</li>
                        <li>• خدمات التخليص الجمركي</li>
                    </ul>
                </div>
                <div class="bg-white p-8 rounded-lg shadow-lg">
                    <h3 class="text-2xl font-semibold mb-4 text-brako-teal">خدمات إضافية</h3>
                    <ul class="space-y-2 text-gray-700">
                        <li>• تغليف احترافي</li>
                        <li>• تأمين الشحنات</li>
                        <li>• تتبع الشحنات</li>
                        <li>• التوصيل للمنزل</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="section-content hidden">
        <div class="container mx-auto px-4 py-16">
            <h2 class="text-4xl font-bold text-center mb-12 text-brako-blue">من نحن</h2>
            <div class="bg-white p-8 rounded-lg shadow-lg max-w-4xl mx-auto">
                <p class="text-lg text-gray-700 leading-relaxed mb-6">
                    شركة BRAKO للشحن الدولي هي إحدى الشركات الرائدة في مجال الشحن والنقل الدولي. نحن نقدم خدمات شحن موثوقة وسريعة لعملائنا في جميع أنحاء العالم.
                </p>
                <p class="text-lg text-gray-700 leading-relaxed mb-6">
                    مع سنوات من الخبرة في هذا المجال، نحن ملتزمون بتقديم أفضل الخدمات وضمان وصول شحناتكم بأمان وفي الوقت المحدد.
                </p>
                <div class="grid md:grid-cols-2 gap-8 mt-8">
                    <div>
                        <h3 class="text-xl font-semibold mb-4 text-brako-teal">رؤيتنا</h3>
                        <p class="text-gray-700">أن نكون الشركة الرائدة في مجال الشحن الدولي في المنطقة</p>
                    </div>
                    <div>
                        <h3 class="text-xl font-semibold mb-4 text-brako-teal">مهمتنا</h3>
                        <p class="text-gray-700">تقديم خدمات شحن عالية الجودة بأسعار تنافسية</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section-content hidden">
        <div class="container mx-auto px-4 py-16">
            <h2 class="text-4xl font-bold text-center mb-12 text-brako-blue">تواصل معنا</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="bg-white p-8 rounded-lg shadow-lg">
                    <h3 class="text-2xl font-semibold mb-6 text-brako-teal">مكتب القامشلي</h3>
                    <div class="space-y-4">
                        <div class="flex items-center space-x-3 space-x-reverse">
                            <span class="text-brako-blue text-xl">📞</span>
                            <span>+963943396345</span>
                        </div>
                        <div class="flex items-center space-x-3 space-x-reverse">
                            <span class="text-brako-blue text-xl">📞</span>
                            <span>+963984487359</span>
                        </div>
                        <div class="flex items-start space-x-3 space-x-reverse">
                            <span class="text-brako-blue text-xl">📍</span>
                            <span>القامشلي - شارع العام غرب كازية الفلاحين قبل دوار عفرين</span>
                        </div>
                    </div>
                </div>
                <div class="bg-white p-8 rounded-lg shadow-lg">
                    <h3 class="text-2xl font-semibold mb-6 text-brako-teal">مكتب أربيل</h3>
                    <div class="space-y-4">
                        <div class="flex items-center space-x-3 space-x-reverse">
                            <span class="text-brako-blue text-xl">📞</span>
                            <span>+964750123456</span>
                        </div>
                        <div class="flex items-center space-x-3 space-x-reverse">
                            <span class="text-brako-blue text-xl">📞</span>
                            <span>+964751987654</span>
                        </div>
                        <div class="flex items-start space-x-3 space-x-reverse">
                            <span class="text-brako-blue text-xl">📍</span>
                            <span>أربيل - هفالان مقابل الأسايش العامة</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Admin Section -->
    <section id="admin" class="section-content hidden">
        <div class="container mx-auto px-4 py-8">
            <h2 class="text-3xl font-bold text-center mb-8 text-brako-blue">إدارة الشحنات</h2>
            
            <div id="admin-user-id" class="mb-4 text-center text-sm text-gray-500 hidden">
                <span class="font-semibold">معرف المستخدم: </span><span id="userIdDisplay"></span>
            </div>

            <!-- قائمة التبويب -->
            <div class="flex justify-center mb-8">
                <div class="bg-white rounded-lg shadow-lg p-2">
                    <button id="addShipmentTab" onclick="showAdminTab('addShipment')" class="px-6 py-3 rounded-lg font-semibold transition-colors bg-brako-blue text-white">
                        إضافة شحنة جديدة
                    </button>
                    <button id="shipmentsListTab" onclick="showAdminTab('shipmentsList')" class="px-6 py-3 rounded-lg font-semibold transition-colors text-brako-blue hover:bg-gray-100">
                        قائمة الشحنات
                    </button>
                    <button id="trackingUpdateTab" onclick="showAdminTab('trackingUpdate')" class="px-6 py-3 rounded-lg font-semibold transition-colors text-brako-blue hover:bg-gray-100">
                        تحديث التتبع
                    </button>
                </div>
            </div>

            <!-- قسم إضافة الشحنة -->
            <div id="addShipmentSection" class="admin-tab-content">
                <form id="addShipmentForm" class="bg-white rounded-lg shadow-lg p-8 max-w-6xl mx-auto">
                    <!-- معلومات الشحنة الأساسية -->
                    <div class="border-2 border-brako-blue rounded-lg p-6 mb-6">
                        <h3 class="text-xl font-semibold mb-4 text-brako-blue">معلومات الشحنة</h3>
                        <div class="grid md:grid-cols-4 gap-4">
                            <div>
                                <label class="block text-sm font-medium mb-2">رقم الشحنة</label>
                                <input type="text" id="shipmentNumber" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent" placeholder="رقم الشحنة">
                            </div>
                            <div>
                                <label class="block text-sm font-medium mb-2">رقم الفاتورة</label>
                                <input type="text" id="invoiceNumber" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent" placeholder="رقم الفاتورة">
                            </div>
                            <div>
                                <label class="block text-sm font-medium mb-2">التاريخ</label>
                                <input type="date" id="shipmentDate" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent">
                            </div>
                            <div>
                                <label class="block text-sm font-medium mb-2">الوقت</label>
                                <input type="time" id="shipmentTime" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent">
                            </div>
                        </div>
                        <div class="mt-4">
                            <label class="block text-sm font-medium mb-2">الفرع</label>
                            <select id="branch" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent">
                                <option value="">اختر الفرع</option>
                                <option value="topeka">توبيكا</option>
                                <option value="brako">براكو</option>
                            </select>
                        </div>
                        <div class="mt-4">
                            <label class="block text-sm font-medium mb-2">نوع الشحن</label>
                            <select id="shippingType" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent">
                                <option value="local">محلي</option>
                                <option value="international">دولي</option>
                            </select>
                        </div>
                    </div>

                    <!-- معلومات المرسل والمستلم -->
                    <div class="border-2 border-brako-teal rounded-lg p-6 mb-6">
                        <h3 class="text-xl font-semibold mb-4 text-brako-teal">معلومات المرسل والمستلم</h3>
                        <div class="grid md:grid-cols-2 gap-8">
                            <div>
                                <h4 class="font-semibold mb-3 text-brako-blue">معلومات المرسل</h4>
                                <div class="space-y-4">
                                    <input type="text" id="senderName" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-teal focus:border-transparent" placeholder="اسم المرسل">
                                    <div class="flex gap-2">
                                        <input type="text" id="senderCountryCode" class="w-20 p-3 border border-gray-300 rounded-lg bg-gray-100 text-center font-semibold" readonly placeholder="+00">
                                        <input type="tel" id="senderPhone" class="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-teal focus:border-transparent" placeholder="رقم الهاتف">
                                    </div>
                                    <select id="senderCountry" onchange="updateCountryCode('sender')" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-teal focus:border-transparent">
                                        <option value="">اختر الدولة</option>
                                        <option value="syria" data-code="+963">سوريا</option>
                                        <option value="iraq" data-code="+964">العراق</option>
                                        <option value="turkey" data-code="+90">تركيا</option>
                                        <option value="germany" data-code="+49">ألمانيا</option>
                                        <option value="netherlands" data-code="+31">هولندا</option>
                                        <option value="france" data-code="+33">فرنسا</option>
                                        <option value="italy" data-code="+39">إيطاليا</option>
                                        <option value="belgium" data-code="+32">بلجيكا</option>
                                        <option value="spain" data-code="+34">إسبانيا</option>
                                        <option value="greece" data-code="+30">اليونان</option>
                                        <option value="uk" data-code="+44">بريطانيا</option>
                                        <option value="sweden" data-code="+46">السويد</option>
                                        <option value="denmark" data-code="+45">الدنمارك</option>
                                    </select>
                                    <select id="senderCity" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-teal focus:border-transparent hidden">
                                        <option value="">اختر المدينة</option>
                                    </select>
                                    <textarea id="senderAddress" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-teal focus:border-transparent" rows="3" placeholder="العنوان التفصيلي"></textarea>
                                </div>
                            </div>
                            <div>
                                <h4 class="font-semibold mb-3 text-brako-blue">معلومات المستلم</h4>
                                <div class="space-y-4">
                                    <input type="text" id="receiverName" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-teal focus:border-transparent" placeholder="اسم المستلم">
                                    <div class="flex gap-2">
                                        <input type="text" id="receiverCountryCode" class="w-20 p-3 border border-gray-300 rounded-lg bg-gray-100 text-center font-semibold" readonly placeholder="+00">
                                        <input type="tel" id="receiverPhone" class="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-teal focus:border-transparent" placeholder="رقم الهاتف">
                                    </div>
                                    <select id="receiverCountry" onchange="updateCountryCode('receiver')" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-teal focus:border-transparent">
                                        <option value="">اختر الدولة</option>
                                        <option value="syria" data-code="+963">سوريا</option>
                                        <option value="iraq" data-code="+964">العراق</option>
                                        <option value="turkey" data-code="+90">تركيا</option>
                                        <option value="germany" data-code="+49">ألمانيا</option>
                                        <option value="netherlands" data-code="+31">هولندا</option>
                                        <option value="france" data-code="+33">فرنسا</option>
                                        <option value="italy" data-code="+39">إيطاليا</option>
                                        <option value="belgium" data-code="+32">بلجيكا</option>
                                        <option value="spain" data-code="+34">إسبانيا</option>
                                        <option value="greece" data-code="+30">اليونان</option>
                                        <option value="uk" data-code="+44">بريطانيا</option>
                                        <option value="sweden" data-code="+46">السويد</option>
                                        <option value="denmark" data-code="+45">الدنمارك</option>
                                    </select>
                                    <select id="receiverCity" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-teal focus:border-transparent hidden">
                                        <option value="">اختر المدينة</option>
                                    </select>
                                    <textarea id="receiverAddress" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-teal focus:border-transparent" rows="3" placeholder="العنوان التفصيلي"></textarea>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- طريقة الدفع والتأمين والتغليف -->
                    <div class="border-2 border-brako-yellow rounded-lg p-6 mb-6">
                        <h3 class="text-xl font-semibold mb-4 text-brako-blue">طريقة الدفع والخدمات الإضافية</h3>
                        <div class="grid md:grid-cols-3 gap-6">
                            <div>
                                <label class="block text-sm font-medium mb-2">طريقة الدفع</label>
                                <select id="paymentMethod" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-yellow focus:border-transparent">
                                    <option value="prepaid">دفع مقدم</option>
                                    <option value="cod">دفع عكسي</option>
                                </select>
                            </div>
                            <div>
                                <label class="flex items-center space-x-2 space-x-reverse">
                                    <input type="checkbox" id="insurance" onchange="toggleInsurance()" class="w-5 h-5 text-brako-blue">
                                    <span class="text-sm font-medium">التأمين</span>
                                </label>
                                <div id="insuranceDetails" class="mt-2 hidden">
                                    <input type="number" id="insuranceCost" class="w-full p-2 border border-gray-300 rounded-lg" placeholder="تكلفة التأمين" oninput="calculateTotal()">
                                </div>
                            </div>
                            <div>
                                <label class="flex items-center space-x-2 space-x-reverse">
                                    <input type="checkbox" id="packaging" onchange="togglePackaging()" class="w-5 h-5 text-brako-blue">
                                    <span class="text-sm font-medium">التغليف</span>
                                </label>
                                <div id="packagingDetails" class="mt-2 hidden">
                                    <input type="number" id="packagingCost" class="w-full p-2 border border-gray-300 rounded-lg" placeholder="تكلفة التغليف" oninput="calculateTotal()">
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- تفاصيل الطرد -->
                    <div class="border-2 border-brako-blue rounded-lg p-6 mb-6">
                        <h3 class="text-2xl font-bold mb-4 text-brako-blue">تفاصيل الطرد</h3>
                        <div class="grid md:grid-cols-5 gap-4 mb-4">
                            <div>
                                <label class="block text-sm font-medium mb-2">العدد</label>
                                <input type="number" id="quantity" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent" placeholder="العدد" oninput="calculateTotal()">
                            </div>
                            <div>
                                <label class="block text-sm font-medium mb-2">السعر الإفرادي</label>
                                <input type="number" id="unitPrice" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent" placeholder="السعر الإفرادي" oninput="calculateTotal()">
                            </div>
                            <div>
                                <label class="block text-sm font-medium mb-2">الوزن (كغ)</label>
                                <input type="number" id="weight" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent" placeholder="الوزن" oninput="calculateTotal()">
                            </div>
                            <div>
                                <label class="block text-sm font-medium mb-2">النوع</label>
                                <input type="text" id="itemType" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent" placeholder="نوع البضاعة">
                            </div>
                            <div>
                                <label class="block text-sm font-medium mb-2">محتويات الطرد</label>
                                <input type="text" id="contents" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent" placeholder="المحتويات">
                            </div>
                        </div>
                        
                        <!-- السعر النهائي -->
                        <div class="bg-gray-50 p-4 rounded-lg">
                            <div class="grid md:grid-cols-4 gap-4 text-lg mb-4">
                                <div>
                                    <span class="font-semibold">السعر الأساسي: </span>
                                    <span id="basePrice" class="text-brako-blue font-bold">0</span>
                                </div>
                                <div>
                                    <span class="font-semibold">التأمين: </span>
                                    <span id="insuranceDisplay" class="text-brako-teal font-bold">0</span>
                                </div>
                                <div>
                                    <span class="font-semibold">التغليف: </span>
                                    <span id="packagingDisplay" class="text-brako-yellow font-bold">0</span>
                                </div>
                                <div>
                                    <label class="block text-sm font-medium mb-2">العملة</label>
                                    <select id="currency" onchange="updateCurrencyDisplay()" class="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent">
                                        <option value="USD">دولار أمريكي (USD)</option>
                                        <option value="SYP">ليرة سورية (SYP)</option>
                                        <option value="IQD">دينار عراقي (IQD)</option>
                                    </select>
                                </div>
                            </div>
                            <div class="bg-brako-blue text-white p-3 rounded text-center">
                                <span class="font-semibold">السعر النهائي: </span>
                                <span id="finalPrice" class="font-bold text-xl">0</span>
                                <span id="currencySymbol" class="font-bold text-xl">USD</span>
                            </div>
                        </div>
                    </div>

                    <!-- أزرار الحفظ والطباعة -->
                    <div class="flex justify-center space-x-4 space-x-reverse">
                        <button type="button" onclick="saveShipment()" class="bg-brako-blue text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-700 transition-colors">
                            حفظ الشحنة
                        </button>
                        <button type="button" onclick="printShipment()" class="bg-brako-teal text-white px-8 py-3 rounded-lg font-semibold hover:bg-teal-700 transition-colors">
                            طباعة الشحنة
                        </button>
                        <button type="button" onclick="sendWhatsApp()" class="bg-green-500 text-white px-8 py-3 rounded-lg font-semibold hover:bg-green-600 transition-colors">
                            📱 إرسال واتساب
                        </button>
                    </div>
                </form>
            </div>

            <!-- قسم قائمة الشحنات -->
            <div id="shipmentsListSection" class="admin-tab-content hidden">
                <div class="bg-white rounded-lg shadow-lg p-6">
                    <h3 class="text-xl font-semibold text-brako-teal mb-6">جميع الشحنات</h3>
                    
                    <!-- شريط البحث -->
                    <div class="mb-6 flex gap-4">
                        <input type="text" id="searchInput" class="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent" placeholder="البحث برقم الشحنة، رقم الفاتورة، أو كود التتبع">
                        <button onclick="searchShipments()" class="bg-brako-blue text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition-colors">
                            بحث
                        </button>
                        <button onclick="clearSearch()" class="bg-gray-500 text-white px-6 py-3 rounded-lg font-semibold hover:bg-gray-600 transition-colors">
                            مسح
                        </button>
                        <button onclick="exportToExcel()" class="bg-green-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-green-700 transition-colors">
                            📊 تصدير إكسل
                        </button>
                    </div>
                    
                    <div id="shipmentsTable" class="overflow-x-auto">
                        <table class="w-full border-collapse border border-gray-300">
                            <thead>
                                <tr class="bg-brako-blue text-white">
                                    <th class="border border-gray-300 p-3">رقم الشحنة</th>
                                    <th class="border border-gray-300 p-3">كود التتبع</th>
                                    <th class="border border-gray-300 p-3">التاريخ</th>
                                    <th class="border border-gray-300 p-3">المرسل</th>
                                    <th class="border border-gray-300 p-3">المستلم</th>
                                    <th class="border border-gray-300 p-3">الوزن</th>
                                    <th class="border border-gray-300 p-3">السعر النهائي</th>
                                    <th class="border border-gray-300 p-3">الحالة</th>
                                    <th class="border border-gray-300 p-3">الإجراءات</th>
                                </tr>
                            </thead>
                            <tbody id="shipmentsTableBody">
                                <!-- سيتم ملء المحتوى ديناميكياً -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- قسم تحديث حالات التتبع -->
            <div id="trackingUpdateSection" class="admin-tab-content hidden">
                <div class="bg-white rounded-lg shadow-lg p-6">
                    <h3 class="text-xl font-semibold text-brako-teal mb-6">تحديث حالات التتبع</h3>
                    
                    <!-- البحث لتحديث الحالة -->
                    <div class="mb-6 flex gap-4">
                        <input type="text" id="trackingSearchInput" class="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent" placeholder="البحث برقم الشحنة أو رقم الفاتورة">
                        <button onclick="searchForTracking()" class="bg-brako-blue text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition-colors">
                            بحث
                        </button>
                    </div>
                    
                    <!-- نتائج البحث لتحديث الحالة -->
                    <div id="trackingResults" class="hidden">
                        <div class="mb-4">
                            <label class="flex items-center space-x-2 space-x-reverse mb-4">
                                <input type="checkbox" id="selectAllTracking" onchange="toggleSelectAllTracking()" class="w-5 h-5 text-brako-blue">
                                <span class="font-semibold">تحديد الكل</span>
                            </label>
                        </div>
                        
                        <div id="trackingShipmentsList" class="mb-6"></div>
                        
                        <div class="grid md:grid-cols-3 gap-4 mb-6">
                            <div>
                                <label class="block text-sm font-medium mb-2">الحالة الجديدة</label>
                                <select id="newStatus" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent">
                                    <option value="received">استلام في المركز</option>
                                    <option value="departed">انطلاق الشحنة</option>
                                    <option value="at_border">في المعبر</option>
                                    <option value="in_transit">في الطريق</option>
                                    <option value="arrived_city">وصول إلى المدينة</option>
                                    <option value="ready_pickup">جاهز للاستلام</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-sm font-medium mb-2">المدينة الحالية</label>
                                <select id="currentCity" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent">
                                    <option value="">اختر المدينة</option>
                                    <option value="دمشق">دمشق</option>
                                    <option value="حمص">حمص</option>
                                    <option value="القامشلي">القامشلي</option>
                                    <option value="حلب">حلب</option>
                                    <option value="الرقة">الرقة</option>
                                    <option value="دير الزور">دير الزور</option>
                                    <option value="المالكية">المالكية</option>
                                    <option value="معبدة">معبدة</option>
                                    <option value="الجوادية">الجوادية</option>
                                    <option value="القحطانية">القحطانية</option>
                                    <option value="عامودا">عامودا</option>
                                    <option value="الدرباسية">الدرباسية</option>
                                    <option value="الحسكة">الحسكة</option>
                                    <option value="كوباني">كوباني</option>
                                    <option value="أربيل">أربيل</option>
                                    <option value="دهوك">دهوك</option>
                                    <option value="دوميز">دوميز</option>
                                    <option value="السليمانية">السليمانية</option>
                                    <option value="زاخو">زاخو</option>
                                    <option value="فايدة">فايدة</option>
                                    <option value="كركوك">كركوك</option>
                                    <option value="كويلان">كويلان</option>
                                    <option value="دار شكران">دار شكران</option>
                                    <option value="قوشتبه">قوشتبه</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-sm font-medium mb-2">ملاحظات</label>
                                <input type="text" id="statusNotes" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent" placeholder="ملاحظات إضافية">
                            </div>
                        </div>
                        
                        <button onclick="updateSelectedStatuses()" class="bg-brako-teal text-white px-8 py-3 rounded-lg font-semibold hover:bg-teal-700 transition-colors">
                            تحديث الحالات المحددة
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- صفحة تفاصيل الشحنة -->
    <section id="shipmentDetails" class="section-content hidden">
        <div class="container mx-auto px-4 py-8">
            <div class="bg-white rounded-lg shadow-lg p-8 max-w-4xl mx-auto">
                <div class="flex justify-between items-center mb-6">
                    <h2 class="text-3xl font-bold text-brako-blue">تفاصيل الشحنة</h2>
                    <button onclick="showSection('admin'); showAdminTab('shipmentsList')" class="bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-600 transition-colors">
                        العودة
                    </button>
                </div>
                
                <div id="shipmentDetailsContent">
                    <!-- سيتم ملء المحتوى ديناميكياً -->
                </div>
                
                <div class="flex justify-center space-x-4 space-x-reverse mt-8">
                    <button onclick="editShipment()" class="bg-brako-blue text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition-colors">
                        تعديل
                    </button>
                    <button onclick="saveShipmentChanges()" class="bg-brako-teal text-white px-6 py-3 rounded-lg font-semibold hover:bg-teal-700 transition-colors hidden" id="saveChangesBtn">
                        حفظ التعديل
                    </button>
                    <button onclick="printShipmentDetails()" class="bg-brako-yellow text-white px-6 py-3 rounded-lg font-semibold hover:bg-yellow-600 transition-colors">
                        طباعة
                    </button>
                    <button onclick="deleteShipmentFromDetails()" class="bg-red-500 text-white px-6 py-3 rounded-lg font-semibold hover:bg-red-600 transition-colors">
                        حذف
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- صفحة تتبع الشحنة للعميل -->
    <section id="customerTracking" class="section-content hidden">
        <div class="gradient-bg text-white py-12">
            <div class="container mx-auto px-4 text-center">
                <h1 class="text-4xl font-bold mb-6">تتبع الشحنة</h1>
                <p class="text-xl">تابع حالة شحنتك في الوقت الفعلي</p>
            </div>
        </div>
        
        <div class="container mx-auto px-4 py-16">
            <div class="bg-white rounded-lg shadow-lg p-8 max-w-2xl mx-auto">
                <h3 class="text-2xl font-semibold text-brako-blue mb-6 text-center">أدخل كود التتبع</h3>
                
                <div class="flex gap-4 mb-8">
                    <input type="text" id="trackingCode" class="flex-1 p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brako-blue focus:border-transparent text-lg" placeholder="أدخل كود التتبع">
                    <button onclick="trackShipment()" class="bg-brako-blue text-white px-8 py-4 rounded-lg font-semibold hover:bg-blue-700 transition-colors">
                        تتبع
                    </button>
                </div>
                
                <div id="trackingResult" class="hidden">
                    <!-- نتائج التتبع -->
                </div>
            </div>
        </div>
    </section>
    
    <!-- نافذة منبثقة مخصصة (Modal) -->
    <div id="customModal" class="modal fixed inset-0 bg-gray-900 bg-opacity-50 flex items-center justify-center z-[1000] hidden">
        <div class="bg-white p-8 rounded-lg shadow-lg max-w-sm w-full mx-4">
            <h3 id="modalTitle" class="text-xl font-bold mb-4 text-brako-blue"></h3>
            <p id="modalMessage" class="mb-6 text-gray-700"></p>
            <div class="flex justify-end space-x-4 space-x-reverse">
                <button id="modalConfirmBtn" class="bg-brako-blue text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors hidden">موافق</button>
                <button id="modalCancelBtn" class="bg-gray-300 text-gray-800 px-6 py-2 rounded-lg hover:bg-gray-400 transition-colors hidden">إلغاء</button>
                <button id="modalOKBtn" class="bg-brako-blue text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors hidden">حسناً</button>
            </div>
        </div>
    </div>

    <!-- سكريبت التطبيق -->
    <script>
        // قاموس المدن للدول العربية
        const citiesData = {
            syria: ['دمشق', 'حمص', 'القامشلي', 'حلب', 'الرقة', 'دير الزور', 'المالكية', 'معبدة', 'الجوادية', 'القحطانية', 'عامودا', 'الدرباسية', 'الحسكة', 'كوباني'],
            iraq: ['أربيل', 'دهوك', 'دوميز', 'السليمانية', 'زاخو', 'فايدة', 'كركوك', 'كويلان', 'دار شكران', 'قوشتبه']
        };

        // دالة لعرض نافذة منبثقة مخصصة
        function customAlert(message) {
            return new Promise(resolve => {
                const modal = document.getElementById('customModal');
                document.getElementById('modalTitle').textContent = 'تنبيه';
                document.getElementById('modalMessage').textContent = message;
                document.getElementById('modalOKBtn').classList.remove('hidden');
                document.getElementById('modalConfirmBtn').classList.add('hidden');
                document.getElementById('modalCancelBtn').classList.add('hidden');
                modal.classList.remove('hidden');

                document.getElementById('modalOKBtn').onclick = () => {
                    modal.classList.add('hidden');
                    resolve();
                };
            });
        }

        // دالة لعرض نافذة تأكيد مخصصة
        function customConfirm(message) {
            return new Promise(resolve => {
                const modal = document.getElementById('customModal');
                document.getElementById('modalTitle').textContent = 'تأكيد';
                document.getElementById('modalMessage').textContent = message;
                document.getElementById('modalConfirmBtn').classList.remove('hidden');
                document.getElementById('modalCancelBtn').classList.remove('hidden');
                document.getElementById('modalOKBtn').classList.add('hidden');
                modal.classList.remove('hidden');

                document.getElementById('modalConfirmBtn').onclick = () => {
                    modal.classList.add('hidden');
                    resolve(true);
                };
                document.getElementById('modalCancelBtn').onclick = () => {
                    modal.classList.add('hidden');
                    resolve(false);
                };
            });
        }

        // تحديث كود الدولة وإظهار المدن
        function updateCountryCode(type) {
            const countrySelect = document.getElementById(type + 'Country');
            const countryCodeInput = document.getElementById(type + 'CountryCode');
            const citySelect = document.getElementById(type + 'City');
            
            const selectedOption = countrySelect.options[countrySelect.selectedIndex];
            const countryCode = selectedOption.getAttribute('data-code') || '+00';
            const countryValue = selectedOption.value;
            
            countryCodeInput.value = countryCode;
            
            if (citiesData[countryValue]) {
                citySelect.classList.remove('hidden');
                citySelect.innerHTML = '<option value="">اختر المدينة</option>';
                citiesData[countryValue].forEach(city => {
                    const option = document.createElement('option');
                    option.value = city;
                    option.textContent = city;
                    citySelect.appendChild(option);
                });
            } else {
                citySelect.classList.add('hidden');
                citySelect.innerHTML = '<option value="">اختر المدينة</option>';
            }
        }

        // إظهار القسم المحدد
        function showSection(sectionId) {
            const sections = document.querySelectorAll('.section-content');
            sections.forEach(section => section.classList.add('hidden'));
            document.getElementById(sectionId).classList.remove('hidden');
        }

        // تفعيل/إلغاء تفعيل التأمين
        function toggleInsurance() {
            const checkbox = document.getElementById('insurance');
            const details = document.getElementById('insuranceDetails');
            if (checkbox.checked) {
                details.classList.remove('hidden');
            } else {
                details.classList.add('hidden');
                document.getElementById('insuranceCost').value = '';
                calculateTotal();
            }
        }

        // تفعيل/إلغاء تفعيل التغليف
        function togglePackaging() {
            const checkbox = document.getElementById('packaging');
            const details = document.getElementById('packagingDetails');
            if (checkbox.checked) {
                details.classList.remove('hidden');
            } else {
                details.classList.add('hidden');
                document.getElementById('packagingCost').value = '';
                calculateTotal();
            }
        }

        // حساب السعر النهائي
        function calculateTotal() {
            const weight = parseFloat(document.getElementById('weight').value) || 0;
            const unitPrice = parseFloat(document.getElementById('unitPrice').value) || 0;
            const insuranceCost = parseFloat(document.getElementById('insuranceCost').value) || 0;
            const packagingCost = parseFloat(document.getElementById('packagingCost').value) || 0;

            const basePrice = weight * unitPrice;
            const finalPrice = basePrice + insuranceCost + packagingCost;

            document.getElementById('basePrice').textContent = basePrice.toFixed(2);
            document.getElementById('insuranceDisplay').textContent = insuranceCost.toFixed(2);
            document.getElementById('packagingDisplay').textContent = packagingCost.toFixed(2);
            document.getElementById('finalPrice').textContent = finalPrice.toFixed(2);
        }

        // تحديث عرض العملة
        function updateCurrencyDisplay() {
            const currency = document.getElementById('currency').value;
            document.getElementById('currencySymbol').textContent = currency;
            calculateTotal();
        }

        // إرسال رسالة واتساب
        function sendWhatsApp() {
            const shipmentNumber = document.getElementById('shipmentNumber').value;
            const senderName = document.getElementById('senderName').value;
            const receiverName = document.getElementById('receiverName').value;
            const receiverCountry = document.getElementById('receiverCountry').options[document.getElementById('receiverCountry').selectedIndex].text;
            const trackingCode = document.getElementById('trackingCode').value || generateTrackingCode();
            
            if (!shipmentNumber || !senderName || !receiverName) {
                customAlert('يرجى ملء البيانات الأساسية قبل إرسال الرسالة');
                return;
            }
            
            const message = `🚚 *شركة BRAKO للشحن الدولي* 🚚

✅ *تم إنشاء شحنتكم بنجاح!*

📋 *تفاصيل الشحنة:*
• رقم الشحنة: *${shipmentNumber}*
• كود التتبع: *${trackingCode}*
• المرسل: ${senderName}
• المستلم: ${receiverName}
• الوجهة: ${receiverCountry}

🔍 *لتتبع شحنتكم:*
${window.location.origin}${window.location.pathname}#tracking

📞 *للاستفسار:*
+963943396345
+963984487359

🙏 *شكراً لثقتكم بنا*
نحن نعمل على توصيل شحنتكم بأمان وسرعة`;
            
            // فتح واتساب ويب مع الرسالة
            const whatsappUrl = `https://web.whatsapp.com/send?text=${encodeURIComponent(message)}`;
            window.open(whatsappUrl, '_blank');
        }

        // توليد كود التتبع
        function generateTrackingCode() {
            return 'BRK' + Date.now().toString().slice(-8);
        }

        // إظهار تبويب الإدارة
        function showAdminTab(tabName) {
            const tabs = document.querySelectorAll('.admin-tab-content');
            tabs.forEach(tab => tab.classList.add('hidden'));
            
            document.getElementById('addShipmentTab').className = 'px-6 py-3 rounded-lg font-semibold transition-colors text-brako-blue hover:bg-gray-100';
            document.getElementById('shipmentsListTab').className = 'px-6 py-3 rounded-lg font-semibold transition-colors text-brako-blue hover:bg-gray-100';
            document.getElementById('trackingUpdateTab').className = 'px-6 py-3 rounded-lg font-semibold transition-colors text-brako-blue hover:bg-gray-100';
            
            if (tabName === 'addShipment') {
                document.getElementById('addShipmentSection').classList.remove('hidden');
                document.getElementById('addShipmentTab').className = 'px-6 py-3 rounded-lg font-semibold transition-colors bg-brako-blue text-white';
            } else if (tabName === 'shipmentsList') {
                document.getElementById('shipmentsListSection').classList.remove('hidden');
                document.getElementById('shipmentsListTab').className = 'px-6 py-3 rounded-lg font-semibold transition-colors bg-brako-blue text-white';
                loadShipments();
            } else if (tabName === 'trackingUpdate') {
                document.getElementById('trackingUpdateSection').classList.remove('hidden');
                document.getElementById('trackingUpdateTab').className = 'px-6 py-3 rounded-lg font-semibold transition-colors bg-brako-blue text-white';
            }
        }

        // البحث في الشحنات
        function searchShipments() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const allShipments = JSON.parse(localStorage.getItem('shipments') || '[]');
            
            if (!searchTerm) {
                displayShipments(allShipments);
                return;
            }
            
            const filteredShipments = allShipments.filter(shipment => 
                (shipment.shipmentNumber && shipment.shipmentNumber.toLowerCase().includes(searchTerm)) ||
                (shipment.invoiceNumber && shipment.invoiceNumber.toLowerCase().includes(searchTerm)) ||
                (shipment.trackingCode && shipment.trackingCode.toLowerCase().includes(searchTerm)) ||
                (shipment.sender && shipment.sender.name && shipment.sender.name.toLowerCase().includes(searchTerm)) ||
                (shipment.receiver && shipment.receiver.name && shipment.receiver.name.toLowerCase().includes(searchTerm))
            );
            
            displayShipments(filteredShipments);
        }

        // مسح البحث
        function clearSearch() {
            document.getElementById('searchInput').value = '';
            searchShipments();
        }

        // البحث لتحديث التتبع
        function searchForTracking() {
            const searchTerm = document.getElementById('trackingSearchInput').value.toLowerCase();
            if (!searchTerm) {
                customAlert('يرجى إدخال رقم الشحنة أو رقم الفاتورة');
                return;
            }
            
            const shipments = JSON.parse(localStorage.getItem('shipments') || '[]');
            const filteredShipments = shipments.filter(shipment => 
                (shipment.shipmentNumber && shipment.shipmentNumber.toLowerCase().includes(searchTerm)) ||
                (shipment.invoiceNumber && shipment.invoiceNumber.toLowerCase().includes(searchTerm))
            );
            
            if (filteredShipments.length === 0) {
                customAlert('لم يتم العثور على شحنات');
                return;
            }
            
            displayTrackingResults(filteredShipments);
        }

        // عرض نتائج البحث للتتبع
        function displayTrackingResults(shipments) {
            const resultsDiv = document.getElementById('trackingResults');
            const listDiv = document.getElementById('trackingShipmentsList');
            
            listDiv.innerHTML = '';
            
            shipments.forEach(shipment => {
                const div = document.createElement('div');
                div.className = 'bg-gray-50 p-4 rounded-lg mb-3';
                div.innerHTML = `
                    <label class="flex items-center space-x-3 space-x-reverse">
                        <input type="checkbox" class="tracking-checkbox w-5 h-5 text-brako-blue" data-id="${shipment.id}">
                        <div class="flex-1">
                            <div class="font-semibold">رقم الشحنة: ${shipment.shipmentNumber}</div>
                            <div class="text-sm text-gray-600">المرسل: ${shipment.sender.name} - المستلم: ${shipment.receiver.name}</div>
                            <div class="text-sm text-gray-600">الحالة الحالية: ${getStatusText(shipment.status || 'received')}</div>
                        </div>
                    </label>
                `;
                listDiv.appendChild(div);
            });
            
            resultsDiv.classList.remove('hidden');
        }

        // تحديد/إلغاء تحديد الكل
        function toggleSelectAllTracking() {
            const selectAll = document.getElementById('selectAllTracking');
            const checkboxes = document.querySelectorAll('.tracking-checkbox');
            
            checkboxes.forEach(checkbox => {
                checkbox.checked = selectAll.checked;
            });
        }

        // تحديث الحالات المحددة
        async function updateSelectedStatuses() {
            const checkboxes = document.querySelectorAll('.tracking-checkbox:checked');
            const newStatus = document.getElementById('newStatus').value;
            const currentCity = document.getElementById('currentCity').value;
            const statusNotes = document.getElementById('statusNotes').value;
            
            if (checkboxes.length === 0) {
                customAlert('يرجى تحديد شحنة واحدة على الأقل');
                return;
            }
            
            const confirmed = await customConfirm('هل أنت متأكد من تحديث حالات الشحنات المحددة؟');
            if (!confirmed) {
                return;
            }

            const shipments = JSON.parse(localStorage.getItem('shipments') || '[]');
            const now = new Date();
            
            checkboxes.forEach(checkbox => {
                const shipmentId = parseInt(checkbox.getAttribute('data-id'));
                const shipmentIndex = shipments.findIndex(s => s.id === shipmentId);
                
                if (shipmentIndex !== -1) {
                    if (!shipments[shipmentIndex].statusHistory) {
                        shipments[shipmentIndex].statusHistory = [];
                    }
                    
                    shipments[shipmentIndex].status = newStatus;
                    shipments[shipmentIndex].currentCity = currentCity;
                    shipments[shipmentIndex].statusHistory.push({
                        status: newStatus,
                        city: currentCity,
                        notes: statusNotes,
                        date: now.toISOString().split('T')[0],
                        time: now.toTimeString().split(' ')[0].substring(0, 5)
                    });
                }
            });
            
            localStorage.setItem('shipments', JSON.stringify(shipments));
            customAlert('تم تحديث الحالات بنجاح');
            
            document.getElementById('trackingResults').classList.add('hidden');
            document.getElementById('trackingSearchInput').value = '';
            loadShipments();
        }

        // الحصول على نص الحالة
        function getStatusText(status) {
            const statusTexts = {
                'received': 'استلام في المركز',
                'departed': 'انطلاق الشحنة',
                'at_border': 'في المعبر',
                'in_transit': 'في الطريق',
                'arrived_city': 'وصول إلى المدينة',
                'ready_pickup': 'جاهز للاستلام'
            };
            return statusTexts[status] || 'غير محدد';
        }

        // تتبع الشحنة للعميل
        function trackShipment() {
            const trackingCode = document.getElementById('trackingCode').value;
            if (!trackingCode) {
                customAlert('يرجى إدخال كود التتبع');
                return;
            }
            
            const shipments = JSON.parse(localStorage.getItem('shipments') || '[]');
            const shipment = shipments.find(s => s.trackingCode === trackingCode);
            
            if (!shipment) {
                customAlert('كود التتبع غير صحيح');
                return;
            }
            
            displayTrackingInfo(shipment);
        }

        // عرض معلومات التتبع
        function displayTrackingInfo(shipment) {
            const resultDiv = document.getElementById('trackingResult');
            
            let statusHistoryHtml = '';
            if (shipment.statusHistory && shipment.statusHistory.length > 0) {
                statusHistoryHtml = shipment.statusHistory.map(status => `
                    <div class="flex justify-between items-center p-3 bg-gray-50 rounded-lg mb-2">
                        <div>
                            <div class="font-semibold">${getStatusText(status.status)}</div>
                            ${status.city ? `<div class="text-sm text-gray-600">المدينة: ${status.city}</div>` : ''}
                            ${status.notes ? `<div class="text-sm text-gray-600">ملاحظات: ${status.notes}</div>` : ''}
                        </div>
                        <div class="text-sm text-gray-500">
                            ${status.date} - ${status.time}
                        </div>
                    </div>
                `).join('');
            } else {
                statusHistoryHtml = '<div class="text-center text-gray-500 p-4">لا توجد تحديثات للحالة</div>';
            }
            
            resultDiv.innerHTML = `
                <div class="border-t pt-6">
                    <h4 class="text-xl font-semibold text-brako-blue mb-4">معلومات الشحنة</h4>
                    <div class="grid md:grid-cols-2 gap-4 mb-6">
                        <div>
                            <strong>رقم الشحنة:</strong> ${shipment.shipmentNumber}
                        </div>
                        <div>
                            <strong>كود التتبع:</strong> ${shipment.trackingCode}
                        </div>
                        <div>
                            <strong>المرسل:</strong> ${shipment.sender.name}
                        </div>
                        <div>
                            <strong>المستلم:</strong> ${shipment.receiver.name}
                        </div>
                        <div>
                            <strong>من:</strong> ${shipment.sender.country}
                        </div>
                        <div>
                            <strong>إلى:</strong> ${shipment.receiver.country}
                        </div>
                    </div>
                    
                    <h4 class="text-xl font-semibold text-brako-teal mb-4">تاريخ الحالات</h4>
                    <div class="space-y-2">
                        ${statusHistoryHtml}
                    </div>
                </div>
            `;
            
            resultDiv.classList.remove('hidden');
        }

        // حفظ الشحنة
        async function saveShipment() {
            const shipmentNumber = document.getElementById('shipmentNumber').value;
            const senderName = document.getElementById('senderName').value;
            const receiverName = document.getElementById('receiverName').value;

            if (!shipmentNumber || !senderName || !receiverName) {
                customAlert('يرجى ملء البيانات الأساسية (رقم الشحنة، اسم المرسل، اسم المستلم)');
                return;
            }

            const trackingCode = generateTrackingCode();
            const currency = document.getElementById('currency').value;
            const now = new Date();

            const shipmentData = {
                id: Date.now(),
                shipmentNumber: shipmentNumber,
                invoiceNumber: document.getElementById('invoiceNumber').value,
                trackingCode: trackingCode,
                date: document.getElementById('shipmentDate').value,
                time: document.getElementById('shipmentTime').value,
                branch: document.getElementById('branch').value,
                shippingType: document.getElementById('shippingType').value,
                sender: {
                    name: senderName,
                    phone: document.getElementById('senderCountryCode').value + ' ' + document.getElementById('senderPhone').value,
                    country: document.getElementById('senderCountry').options[document.getElementById('senderCountry').selectedIndex].text,
                    city: document.getElementById('senderCity').value,
                    address: document.getElementById('senderAddress').value
                },
                receiver: {
                    name: receiverName,
                    phone: document.getElementById('receiverCountryCode').value + ' ' + document.getElementById('receiverPhone').value,
                    country: document.getElementById('receiverCountry').options[document.getElementById('receiverCountry').selectedIndex].text,
                    city: document.getElementById('receiverCity').value,
                    address: document.getElementById('receiverAddress').value
                },
                paymentMethod: document.getElementById('paymentMethod').value,
                insurance: document.getElementById('insurance').checked,
                insuranceCost: document.getElementById('insuranceCost').value || '0',
                packaging: document.getElementById('packaging').checked,
                packagingCost: document.getElementById('packagingCost').value || '0',
                quantity: document.getElementById('quantity').value,
                unitPrice: document.getElementById('unitPrice').value,
                weight: document.getElementById('weight').value,
                itemType: document.getElementById('itemType').value,
                contents: document.getElementById('contents').value,
                finalPrice: document.getElementById('finalPrice').textContent,
                currency: currency,
                status: 'received',
                createdAt: Date.now(), // timestamp for sorting
                statusHistory: [{
                    status: 'received',
                    city: document.getElementById('branch').value === 'topeka' ? 'توبيكا' : 'براكو',
                    notes: 'تم استلام الشحنة في المركز',
                    date: now.toISOString().split('T')[0],
                    time: now.toTimeString().split(' ')[0].substring(0, 5)
                }]
            };

            const confirmed = await customConfirm('هل أنت متأكد من حفظ هذه الشحنة؟');
            if (!confirmed) {
                return;
            }

            try {
                const shipments = JSON.parse(localStorage.getItem('shipments') || '[]');
                shipments.push(shipmentData);
                localStorage.setItem('shipments', JSON.stringify(shipments));
                customAlert(`تم حفظ الشحنة بنجاح!\nكود التتبع: ${trackingCode}`);
                resetForm();
                loadShipments();
            } catch (e) {
                console.error("Error adding document: ", e);
                customAlert("حدث خطأ أثناء حفظ الشحنة. يرجى المحاولة مرة أخرى.");
            }
        }

        // طباعة الشحنة
        function printShipment() {
            const shipmentNumber = document.getElementById('shipmentNumber').value;
            const invoiceNumber = document.getElementById('invoiceNumber').value;
            const senderName = document.getElementById('senderName').value;
            const receiverName = document.getElementById('receiverName').value;
            const finalPrice = document.getElementById('finalPrice').textContent;
            const currency = document.getElementById('currency').value;

            if (!shipmentNumber || !senderName || !receiverName) {
                customAlert('يرجى ملء البيانات الأساسية قبل الطباعة');
                return;
            }

            const trackingCode = generateTrackingCode();
            const senderCountry = document.getElementById('senderCountry').options[document.getElementById('senderCountry').selectedIndex].text;
            const receiverCountry = document.getElementById('receiverCountry').options[document.getElementById('receiverCountry').selectedIndex].text;
            const senderPhone = document.getElementById('senderCountryCode').value + ' ' + document.getElementById('senderPhone').value;
            const receiverPhone = document.getElementById('receiverCountryCode').value + ' ' + document.getElementById('receiverPhone').value;
            const weight = document.getElementById('weight').value;
            const itemType = document.getElementById('itemType').value;
            const contents = document.getElementById('contents').value;
            const paymentMethod = document.getElementById('paymentMethod').value === 'prepaid' ? 'دفع مقدم' : 'دفع عكسي';
            const basePrice = document.getElementById('basePrice').textContent;
            const insuranceCost = document.getElementById('insuranceDisplay').textContent;
            const packagingCost = document.getElementById('packagingDisplay').textContent;

            const printWindow = window.open('', '_blank');
            printWindow.document.write(`
                <html dir="rtl">
                <head>
                    <title>فاتورة شحنة - ${shipmentNumber}</title>
                    <style>
                        body { font-family: 'Cairo', sans-serif; margin: 20px; line-height: 1.6; }
                        .header { text-align: center; margin-bottom: 30px; border-bottom: 3px solid #1e40af; padding-bottom: 20px; }
                        .company-name { color: #1e40af; font-size: 28px; font-weight: bold; margin-bottom: 10px; }
                        .invoice-title { color: #14b8a6; font-size: 22px; margin-bottom: 5px; }
                        .section { margin-bottom: 25px; padding: 15px; border: 1px solid #ddd; border-radius: 8px; background: #f9f9f9; }
                        .section-title { color: #1e40af; font-size: 18px; font-weight: bold; margin-bottom: 15px; border-bottom: 2px solid #1e40af; padding-bottom: 5px; }
                        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 15px; }
                        .info-row { margin-bottom: 8px; }
                        .label { font-weight: bold; color: #374151; }
                        .value { color: #1f2937; }
                        .total-section { background: linear-gradient(135deg, #1e40af, #14b8a6); color: white; padding: 20px; border-radius: 10px; text-align: center; }
                        .total-price { font-size: 24px; font-weight: bold; margin-bottom: 10px; }
                        .footer { text-align: center; margin-top: 30px; padding-top: 20px; border-top: 2px solid #1e40af; color: #6b7280; }
                        .tracking-code { background: #fbbf24; color: #1e40af; padding: 10px; border-radius: 5px; font-weight: bold; text-align: center; margin: 15px 0; }
                    </style>
                </head>
                <body>
                    <div class="header">
                        <div class="company-name">BRAKO - شركة الشحن الدولي</div>
                        <div class="invoice-title">فاتورة شحنة</div>
                        <div style="margin-top: 10px;">
                            <strong>رقم الشحنة:</strong> ${shipmentNumber} | 
                            <strong>رقم الفاتورة:</strong> ${invoiceNumber || 'غير محدد'}
                        </div>
                        <div class="tracking-code">
                            كود التتبع: ${trackingCode}
                        </div>
                    </div>
                    
                    <div class="section">
                        <div class="section-title">معلومات الشحنة</div>
                        <div class="grid">
                            <div class="info-row">
                                <span class="label">التاريخ:</span> 
                                <span class="value">${document.getElementById('shipmentDate').value}</span>
                            </div>
                            <div class="info-row">
                                <span class="label">الوقت:</span> 
                                <span class="value">${document.getElementById('shipmentTime').value}</span>
                            </div>
                            <div class="info-row">
                                <span class="label">الفرع:</span> 
                                <span class="value">${document.getElementById('branch').value === 'topeka' ? 'توبيكا' : 'براكو'}</span>
                            </div>
                            <div class="info-row">
                                <span class="label">نوع الشحن:</span> 
                                <span class="value">${document.getElementById('shippingType').value === 'local' ? 'محلي' : 'دولي'}</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="grid">
                        <div class="section">
                            <div class="section-title">معلومات المرسل</div>
                            <p><strong>الاسم:</strong> ${senderName}</p>
                            <p><strong>الهاتف:</strong> ${senderPhone}</p>
                            <p><strong>الدولة:</strong> ${senderCountry}</p>
                            <p><strong>العنوان:</strong> ${document.getElementById('senderAddress').value}</p>
                        </div>
                        
                        <div class="section">
                            <div class="section-title">معلومات المستلم</div>
                            <p><strong>الاسم:</strong> ${receiverName}</p>
                            <p><strong>الهاتف:</strong> ${receiverPhone}</p>
                            <p><strong>الدولة:</strong> ${receiverCountry}</p>
                            <p><strong>العنوان:</strong> ${document.getElementById('receiverAddress').value}</p>
                        </div>
                    </div>
                    
                    <div class="section">
                        <div class="section-title">تفاصيل الطرد</div>
                        <div class="grid">
                            <div class="info-row"><span class="label">الوزن:</span> <span class="value">${weight} كغ</span></div>
                            <div class="info-row"><span class="label">العدد:</span> <span class="value">${document.getElementById('quantity').value}</span></div>
                            <div class="info-row"><span class="label">نوع البضاعة:</span> <span class="value">${itemType}</span></div>
                            <div class="info-row"><span class="label">المحتويات:</span> <span class="value">${contents}</span></div>
                            <div class="info-row"><span class="label">طريقة الدفع:</span> <span class="value">${paymentMethod}</span></div>
                            <div class="info-row"><span class="label">السعر الإفرادي:</span> <span class="value">${document.getElementById('unitPrice').value} ${currency}</span></div>
                        </div>
                    </div>
                    
                    <div class="section">
                        <div class="section-title">تفاصيل التكلفة</div>
                        <div class="info-row"><span class="label">السعر الأساسي:</span> <span class="value">${basePrice} ${currency}</span></div>
                        <div class="info-row"><span class="label">التأمين:</span> <span class="value">${insuranceCost} ${currency}</span></div>
                        <div class="info-row"><span class="label">التغليف:</span> <span class="value">${packagingCost} ${currency}</span></div>
                    </div>
                    
                    <div class="total-section">
                        <div class="total-price">السعر النهائي: ${finalPrice} ${currency}</div>
                        <div>طريقة الدفع: ${paymentMethod}</div>
                    </div>
                    
                    <div class="footer">
                        <p><strong>شركة BRAKO للشحن الدولي</strong></p>
                        <p>القامشلي: +963943396345 | +963984487359</p>
                        <p>أربيل: +964750123456 | +964751987654</p>
                        <p>شكراً لثقتكم بنا</p>
                    </div>
                </body>
                </html>
            `);
            printWindow.document.close();
            printWindow.print();
        }

        // عرض الشحنات
        function displayShipments(shipments) {
            const tableBody = document.getElementById('shipmentsTableBody');
            
            if (shipments.length === 0) {
                tableBody.innerHTML = '<tr><td colspan="9" class="text-center p-8 text-gray-500">لا توجد شحنات مسجلة</td></tr>';
                return;
            }
            
            // فرز الشحنات من الأحدث إلى الأقدم
            shipments.sort((a, b) => b.createdAt - a.createdAt);
            
            window.allShipments = shipments;
            tableBody.innerHTML = '';
            
            shipments.forEach((shipment, index) => {
                const row = document.createElement('tr');
                row.className = index % 2 === 0 ? 'bg-gray-50' : 'bg-white';
                
                row.innerHTML = `
                    <td class="border border-gray-300 p-3">${shipment.shipmentNumber}</td>
                    <td class="border border-gray-300 p-3">${shipment.trackingCode || 'غير محدد'}</td>
                    <td class="border border-gray-300 p-3">${shipment.date}</td>
                    <td class="border border-gray-300 p-3">${shipment.sender.name}</td>
                    <td class="border border-gray-300 p-3">${shipment.receiver.name}</td>
                    <td class="border border-gray-300 p-3">${shipment.weight} كغ</td>
                    <td class="border border-gray-300 p-3">${shipment.finalPrice} ${shipment.currency || 'USD'}</td>
                    <td class="border border-gray-300 p-3">
                        <span class="px-2 py-1 rounded text-xs font-semibold ${getStatusColor(shipment.status || 'received')}">
                            ${getStatusText(shipment.status || 'received')}
                        </span>
                    </td>
                    <td class="border border-gray-300 p-3">
                        <button onclick="viewShipmentDetails(${shipment.id})" class="bg-brako-teal text-white px-3 py-1 rounded text-sm hover:bg-teal-700 mr-2">عرض</button>
                        <button onclick="deleteShipment(${shipment.id})" class="bg-red-500 text-white px-3 py-1 rounded text-sm hover:bg-red-700">حذف</button>
                    </td>
                `;
                
                tableBody.appendChild(row);
            });
        }
        
        // تحميل قائمة الشحنات
        function loadShipments() {
            const shipments = JSON.parse(localStorage.getItem('shipments') || '[]');
            displayShipments(shipments);
            updateStatistics(shipments);
        }

        // الحصول على لون الحالة
        function getStatusColor(status) {
            const colors = {
                'received': 'bg-blue-100 text-blue-800',
                'departed': 'bg-yellow-100 text-yellow-800',
                'at_border': 'bg-orange-100 text-orange-800',
                'in_transit': 'bg-purple-100 text-purple-800',
                'arrived_city': 'bg-teal-100 text-teal-800',
                'ready_pickup': 'bg-green-100 text-green-800'
            };
            return colors[status] || 'bg-gray-100 text-gray-800';
        }

        // تحديث الإحصائيات
        function updateStatistics(shipments) {
            const totalShipments = shipments.length;
            const deliveredShipments = shipments.filter(s => s.status === 'ready_pickup').length;
            const pendingShipments = totalShipments - deliveredShipments;
            
            let totalRevenue = 0;
            shipments.forEach(shipment => {
                const price = parseFloat(shipment.finalPrice) || 0;
                totalRevenue += price;
            });
            
            document.getElementById('totalShipments').textContent = totalShipments;
            document.getElementById('totalRevenue').textContent = totalRevenue.toFixed(2);
            document.getElementById('deliveredShipments').textContent = deliveredShipments;
            document.getElementById('pendingShipments').textContent = pendingShipments;
        }

        // عرض تفاصيل الشحنة في صفحة منفصلة
        function viewShipmentDetails(id) {
            const shipments = JSON.parse(localStorage.getItem('shipments') || '[]');
            const shipment = shipments.find(s => s.id === id);
            
            if (!shipment) {
                customAlert('لم يتم العثور على الشحنة');
                return;
            }
            
            window.currentShipmentId = id;
            
            const content = document.getElementById('shipmentDetailsContent');
            content.innerHTML = `
                <div class="grid md:grid-cols-2 gap-8">
                    <div class="space-y-6">
                        <div class="bg-brako-blue text-white p-4 rounded-lg">
                            <h3 class="text-lg font-semibold mb-2">معلومات الشحنة</h3>
                            <div class="space-y-2 text-sm">
                                <div><strong>رقم الشحنة:</strong> ${shipment.shipmentNumber}</div>
                                <div><strong>رقم الفاتورة:</strong> ${shipment.invoiceNumber}</div>
                                <div><strong>كود التتبع:</strong> ${shipment.trackingCode || 'غير محدد'}</div>
                                <div><strong>التاريخ:</strong> ${shipment.date} - ${shipment.time}</div>
                                <div><strong>الفرع:</strong> ${shipment.branch === 'topeka' ? 'توبيكا' : 'براكو'}</div>
                                <div><strong>نوع الشحن:</strong> ${shipment.shippingType === 'local' ? 'محلي' : 'دولي'}</div>
                            </div>
                        </div>
                        
                        <div class="bg-brako-teal text-white p-4 rounded-lg">
                            <h3 class="text-lg font-semibold mb-2">معلومات المرسل</h3>
                            <div class="space-y-2 text-sm">
                                <div><strong>الاسم:</strong> ${shipment.sender.name}</div>
                                <div><strong>الهاتف:</strong> ${shipment.sender.phone}</div>
                                <div><strong>الدولة:</strong> ${shipment.sender.country}</div>
                                ${shipment.sender.city ? `<div><strong>المدينة:</strong> ${shipment.sender.city}</div>` : ''}
                                <div><strong>العنوان:</strong> ${shipment.sender.address}</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="space-y-6">
                        <div class="bg-brako-yellow text-white p-4 rounded-lg">
                            <h3 class="text-lg font-semibold mb-2">معلومات المستلم</h3>
                            <div class="space-y-2 text-sm">
                                <div><strong>الاسم:</strong> ${shipment.receiver.name}</div>
                                <div><strong>الهاتف:</strong> ${shipment.receiver.phone}</div>
                                <div><strong>الدولة:</strong> ${shipment.receiver.country}</div>
                                ${shipment.receiver.city ? `<div><strong>المدينة:</strong> ${shipment.receiver.city}</div>` : ''}
                                <div><strong>العنوان:</strong> ${shipment.receiver.address}</div>
                            </div>
                        </div>
                        
                        <div class="bg-gray-100 p-4 rounded-lg">
                            <h3 class="text-lg font-semibold mb-2 text-gray-800">تفاصيل الطرد</h3>
                            <div class="space-y-2 text-sm text-gray-700">
                                <div><strong>الوزن:</strong> ${shipment.weight} كغ</div>
                                <div><strong>العدد:</strong> ${shipment.quantity}</div>
                                <div><strong>نوع البضاعة:</strong> ${shipment.itemType}</div>
                                <div><strong>المحتويات:</strong> ${shipment.contents}</div>
                                <div><strong>السعر النهائي:</strong> ${shipment.finalPrice} ${shipment.currency || 'USD'}</div>
                                <div><strong>طريقة الدفع:</strong> ${shipment.paymentMethod === 'prepaid' ? 'دفع مقدم' : 'دفع عكسي'}</div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="mt-8 bg-white border-2 border-brako-blue rounded-lg p-6">
                    <h3 class="text-xl font-semibold text-brako-blue mb-4">حالة التتبع</h3>
                    <div class="space-y-3">
                        ${shipment.statusHistory ? shipment.statusHistory.map(status => `
                            <div class="flex justify-between items-center p-3 bg-gray-50 rounded-lg">
                                <div>
                                    <div class="font-semibold">${getStatusText(status.status)}</div>
                                    ${status.city ? `<div class="text-sm text-gray-600">المدينة: ${status.city}</div>` : ''}
                                    ${status.notes ? `<div class="text-sm text-gray-600">ملاحظات: ${status.notes}</div>` : ''}
                                </div>
                                <div class="text-sm text-gray-500">
                                    ${status.date} - ${status.time}
                                </div>
                            </div>
                        `).join('') : '<div class="text-center text-gray-500 p-4">لا توجد تحديثات للحالة</div>'}
                    </div>
                </div>
            `;
            
            showSection('shipmentDetails');
        }

        // طباعة تفاصيل الشحنة
        function printShipmentDetails() {
            const shipments = JSON.parse(localStorage.getItem('shipments') || '[]');
            const shipment = shipments.find(s => s.id === window.currentShipmentId);
            
            if (!shipment) {
                customAlert('لم يتم العثور على الشحنة');
                return;
            }
            
            const printWindow = window.open('', '_blank');
            printWindow.document.write(`
                <html dir="rtl">
                <head>
                    <title>فاتورة شحنة - ${shipment.shipmentNumber}</title>
                    <style>
                        body { font-family: 'Cairo', sans-serif; margin: 20px; }
                        .header { text-align: center; margin-bottom: 30px; border-bottom: 2px solid #1e40af; padding-bottom: 20px; }
                        .section { margin-bottom: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 8px; }
                        .total { font-size: 18px; font-weight: bold; color: #1e40af; background: #f0f9ff; padding: 15px; border-radius: 8px; }
                        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
                    </style>
                </head>
                <body>
                    <div class="header">
                        <h1>BRAKO - شركة الشحن الدولي</h1>
                        <h2>فاتورة شحنة رقم: ${shipment.shipmentNumber}</h2>
                        <p>كود التتبع: ${shipment.trackingCode}</p>
                    </div>
                    
                    <div class="grid">
                        <div class="section">
                            <h3>معلومات المرسل</h3>
                            <p><strong>الاسم:</strong> ${shipment.sender.name}</p>
                            <p><strong>الهاتف:</strong> ${shipment.sender.phone}</p>
                            <p><strong>الدولة:</strong> ${shipment.sender.country}</p>
                            <p><strong>العنوان:</strong> ${shipment.sender.address}</p>
                        </div>
                        
                        <div class="section">
                            <h3>معلومات المستلم</h3>
                            <p><strong>الاسم:</strong> ${shipment.receiver.name}</p>
                            <p><strong>الهاتف:</strong> ${shipment.receiver.phone}</p>
                            <p><strong>الدولة:</strong> ${shipment.receiver.country}</p>
                            <p><strong>العنوان:</strong> ${shipment.receiver.address}</p>
                        </div>
                    </div>
                    
                    <div class="section">
                        <h3>تفاصيل الشحنة</h3>
                        <p><strong>التاريخ:</strong> ${shipment.date} - ${shipment.time}</p>
                        <p><strong>الوزن:</strong> ${shipment.weight} كغ</p>
                        <p><strong>نوع البضاعة:</strong> ${shipment.itemType}</p>
                        <p><strong>المحتويات:</strong> ${shipment.contents}</p>
                    </div>
                    
                    <div class="total">
                        <p>السعر النهائي: ${shipment.finalPrice} ${shipment.currency || 'USD'}</p>
                        <p>طريقة الدفع: ${shipment.paymentMethod === 'prepaid' ? 'دفع مقدم' : 'دفع عكسي'}</p>
                    </div>
                </body>
                </html>
            `);
            printWindow.document.close();
            printWindow.print();
        }

        // حذف الشحنة من صفحة التفاصيل
        async function deleteShipmentFromDetails() {
            const confirmed = await customConfirm('هل أنت متأكد من حذف هذه الشحنة؟');
            if (confirmed) {
                deleteShipment(window.currentShipmentId);
                showSection('admin');
                showAdminTab('shipmentsList');
            }
        }

        // حذف الشحنة
        async function deleteShipment(id) {
            const confirmed = await customConfirm('هل أنت متأكد من حذف هذه الشحنة؟');
            if (confirmed) {
                let shipments = JSON.parse(localStorage.getItem('shipments') || '[]');
                shipments = shipments.filter(s => s.id !== id);
                localStorage.setItem('shipments', JSON.stringify(shipments));
                customAlert('تم حذف الشحنة بنجاح');
                loadShipments();
            }
        }

        // إعادة تعيين النموذج
        function resetForm() {
            document.getElementById('addShipmentForm').reset();
            document.getElementById('insuranceDetails').classList.add('hidden');
            document.getElementById('packagingDetails').classList.add('hidden');
            calculateTotal();
            
            const now = new Date();
            document.getElementById('shipmentDate').value = now.toISOString().split('T')[0];
            document.getElementById('shipmentTime').value = now.toTimeString().split(' ')[0].substring(0, 5);
        }

        // تصدير البيانات إلى إكسل
        function exportToExcel() {
            const shipments = JSON.parse(localStorage.getItem('shipments') || '[]');
            
            if (shipments.length === 0) {
                customAlert('لا توجد بيانات للتصدير');
                return;
            }
            
            let csvContent = '\uFEFF';
            csvContent += 'رقم الشحنة,رقم الفاتورة,كود التتبع,التاريخ,المرسل,المستلم,من,إلى,الوزن,السعر النهائي,العملة,الحالة\n';
            
            shipments.forEach(shipment => {
                csvContent += `"${shipment.shipmentNumber}","${shipment.invoiceNumber || ''}","${shipment.trackingCode || ''}","${shipment.date}","${shipment.sender.name}","${shipment.receiver.name}","${shipment.sender.country}","${shipment.receiver.country}","${shipment.weight}","${shipment.finalPrice}","${shipment.currency || 'USD'}","${getStatusText(shipment.status || 'received')}"\n`;
            });
            
            const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement('a');
            const url = URL.createObjectURL(blob);
            link.setAttribute('href', url);
            link.setAttribute('download', `BRAKO_Shipments_${new Date().toISOString().split('T')[0]}.csv`);
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }

        // تفعيل وضع التعديل (ويمكن حفظ التعديل)
        function editShipment() {
            const inputs = document.querySelectorAll('#shipmentDetailsContent input, #shipmentDetailsContent select, #shipmentDetailsContent textarea');
            inputs.forEach(input => {
                input.disabled = false;
                input.style.backgroundColor = '#fff';
                input.style.border = '1px solid #d1d5db';
            });
            document.getElementById('saveChangesBtn').classList.remove('hidden');
            customAlert('يمكنك الآن تعديل البيانات');
        }

        // حفظ التعديلات
        async function saveShipmentChanges() {
            const confirmed = await customConfirm('هل أنت متأكد من حفظ التعديلات؟');
            if (!confirmed) return;

            const shipments = JSON.parse(localStorage.getItem('shipments') || '[]');
            const shipmentIndex = shipments.findIndex(s => s.id === window.currentShipmentId);

            if (shipmentIndex === -1) {
                customAlert('لم يتم العثور على الشحنة');
                return;
            }
            
            // جمع البيانات من الحقول المعدلة (مثال توضيحي)
            const updatedData = {
                shipmentNumber: document.getElementById('shipmentNumber_edit').value,
                invoiceNumber: document.getElementById('invoiceNumber_edit').value,
                sender: {
                    name: document.getElementById('senderName_edit').value
                }
                // ... وهكذا لكل الحقول
            };
            
            // دمج البيانات
            shipments[shipmentIndex] = { ...shipments[shipmentIndex], ...updatedData };
            localStorage.setItem('shipments', JSON.stringify(shipments));
            
            customAlert('تم حفظ التعديلات بنجاح');
            
            // إعادة تحميل التفاصيل
            viewShipmentDetails(window.currentShipmentId);
            document.getElementById('saveChangesBtn').classList.add('hidden');
        }
        
        // دالة لتبديل قائمة التنقل الخاصة بالهاتف
        function toggleMobileMenu() {
            const mobileMenu = document.getElementById('mobile-menu');
            mobileMenu.classList.toggle('hidden');
        }

        // تعيين التاريخ والوقت الحالي عند تحميل الصفحة
        window.onload = function() {
            const now = new Date();
            document.getElementById('shipmentDate').value = now.toISOString().split('T')[0];
            document.getElementById('shipmentTime').value = now.toTimeString().split(' ')[0].substring(0, 5);
            loadShipments();
        };
    </script>
</body>
</html>
